import os
import pandas as pd
from openai import OpenAI as oai
import warnings
from tqdm import tqdm
import logging
from IPython.display import Markdown, display
from llama_index.experimental.query_engine import PandasQueryEngine
import joblib
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from llama_index.core.tools import BaseTool, FunctionTool
from llama_index.core.agent import AgentRunner
from llama_index.agent.openai import OpenAIAgentWorker, OpenAIAgent
from llama_index.core import PromptTemplate
from llama_index.core.query_pipeline import (
    QueryPipeline as QP,
    Link,
    InputComponent,
)
from llama_index.experimental.query_engine.pandas import (
    PandasInstructionParser,
)
from llama_index.llms.openai import OpenAI
from llama_index.core import PromptTemplate
import glob
import nest_asyncio

nest_asyncio.apply()

warnings.filterwarnings('ignore')

class SIPSA_Analyzer:

    def __init__(self, openai_key: str, whisper_model = 'whisper-1'):
        
        self.whisper_model = whisper_model
        self.openai_client =  oai(base_url=None, api_key=openai_key)

        self.data = self._import_data()

        self._load_prompts()

    def _import_data(self):
        df = pd.read_feather('data/data.feather')

        return df
    
    def query_df(self, prompt: str):
        query = 'Para la siguiente petición, siempre consulta el nombre de todos los alimentos en singular y en mayúscula sostenida, y utiliza str.contains() en los strings: ' + prompt + 'en tu respuesta solo responde sobre los datos, no des respuestas adicionales'
        query = query.upper()
        query_engine = PandasQueryEngine(df=self.data, verbose=True, synthesize_response=True)
        #new_prompt = PromptTemplate(self.sys_prompt)
        #query_engine.update_prompts({"pandas_prompt": new_prompt})
        response = query_engine.query(query)
        
        return response.response
    
    def _load_prompts(self):
        sys_prompt_path = 'input/sys_prompt.txt'
        instruction_prompt_path = 'input/instruction_prompt.txt'
        pandas_prompt_path = 'input/pandas_prompt.txt'
        response_synthesis_prompt_path = 'input/response_synthesis_prompt.txt'

        with open(sys_prompt_path, 'r') as f:
            prompt_str = f.read()
        
        with open(instruction_prompt_path, 'r') as f:
            instruction_str = f.read()

        with open(pandas_prompt_path, 'r') as f:
            pandas_prompt_str = f.read()

        with open(response_synthesis_prompt_path, 'r') as f:
            response_synthesis_prompt_str = f.read()

        self.sys_prompt = prompt_str
        self.instruction_prompt = instruction_str
        self.pandas_prompt = pandas_prompt_str
        self.response_synthesis_prompt = response_synthesis_prompt_str

    def pandas_query_pipeline(self, query: str):

        pandas_prompt = PromptTemplate(self.pandas_prompt).partial_format(
            instruction_str = self.instruction_prompt, df_str=self.data.head(5)
        )
        pandas_output_parser = PandasInstructionParser(self.data)
        response_synthesis_prompt = PromptTemplate(self.response_synthesis_prompt)
        llm = OpenAI(model="gpt-3.5-turbo")

        qp = QP(
        modules={
            "input": InputComponent(),
            "pandas_prompt": pandas_prompt,
            "llm1": llm,
            "pandas_output_parser": pandas_output_parser,
            "response_synthesis_prompt": response_synthesis_prompt,
            "llm2": llm,
        },
        verbose=True,
        )
        qp.add_chain(["input", "pandas_prompt", "llm1", "pandas_output_parser"])
        qp.add_links(
            [
                Link("input", "response_synthesis_prompt", dest_key="query_str"),
                Link(
                    "llm1", "response_synthesis_prompt", dest_key="pandas_instructions"
                ),
                Link(
                    "pandas_output_parser",
                    "response_synthesis_prompt",
                    dest_key="pandas_output",
                ),
            ]
        )

        qp.add_link("response_synthesis_prompt", "llm2")

        response = qp.run(query_str=query)

        return response
    
    def get_audio_files(self, folder_path):
        audio_extensions = ["*.aac","*.wav","*.opus","*.ogg","*.mp3","*.mp4","*.mpeg","*.m4a", '*.flac']
        audio_files = []
        for ext in audio_extensions:
            audio_files.extend(glob(os.path.join(folder_path, ext)))
        self.audio_files = audio_files

    def transcribe_audio(self, file_path):
        segments, info = self.audio_model.transcribe(file_path, beam_size=2, language="es",hotwords=self.hotwords)
        self.transcription = " ".join([segment.text for segment in segments])
        print(self.transcription)

    def transcribe_audio_openai(self, audio_file):
        #audio_file = open(file_path, "rb")
        self.transcription = self.openai_client.audio.transcriptions.create(
            model=self.whisper_model, 
            file=audio_file,
            language='es',
            response_format="text",
      )
        print(self.transcription)

    def process_audios(self, folder_path, user_prompt, system_prompt):
        results = []
        audio_files = self.get_audio_files(folder_path)

        for audio_file in tqdm(audio_files):
            transcription = self.transcribe_audio(audio_file)
            table = self.generate_table(transcription, user_prompt, system_prompt)
            results.append({
                "audio_file": os.path.basename(audio_file),
                "transcription": transcription,
                "table": table
            })

        return results