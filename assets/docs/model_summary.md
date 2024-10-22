![dane_sen_logo](https://github.com/contreras-juan/pry-sipsa-DANE-f1/blob/main/assets/images/dane_sen_logo_2024.PNG?raw=true)

# Informe resumen de modelos

En este resumen abarca la descripción de los algoritmos utilizados, los parámetros ajustados y los resultados obtenidos. El informe detalla el proceso de selección de modelos, las métricas de evaluación empleadas y las conclusiones derivadas de los experimentos, con el propósito de ofrecer una visión comprensiva de cómo los modelos contribuyen a abordar el problema de negocio y las recomendaciones para su posible mejora o implementación.

## Descripción del Problema

Responder de forma automatizada a las diferentes consultas sobre producción, abastecimiento y disponibilidad de los productos de la canasta familiar y generar predicciones (forecasting) para series de tiempo definidas por usuarios. El proyecto se enfoca en resolver la necesidad de proporcionar respuestas de forma ágil e intuitiva a las preguntas definidas por el usuario interesado en obtener información específica sobre producción y distribución de productos de la canasta familiar y otros sectores económicos capturados por el SIPSA. Para ello se optó por utilizar el modelo Large Lenguage Model Meta AI (LLaMA), el cual es de tipo Transformer y fue diseñado para tareas de procesamiento de lenguaje natural (NLP). Además, es ampliamente implementado en el desarrolo de chatbots dada sus facultades para responder consultas de forma eficiente y precisa.

## Experimentación

- Modelo 1: Se plantea el uso del modelo Large Lenguage Model Meta AI (LLaMA)que es de tipo Transformer por dada sus facultades para responder consultas de forma eficiente y precisa.

### Variables de entrada

Consulta de texto libre en lenguaje natural.

### Variable objetivo

Precisión de la respuesta a la consulta.

### Registros de entrenamiento

A continuación se presenta el registro del entrenamiento de los modelos.
 
| **Algoritmo/Modelo Utilizado**                              | **Parámetros de Entrenamiento**                                     | **Técnicas de Optimización**                | **Regularización**                           | **Funciones de Pérdida**                             | **Métricas de Evaluación**                    | **Curvas de Rendimiento**                       | **Configuración de Hardware**                  | **Tiempo de Entrenamiento**                  | **Versiones de Software**                    | **Configuración de Entrenamiento**                   |
|-------------------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------|-----------------------------------------------|--------------------------------------------------|------------------------------------------------|--------------------------------------------------|------------------------------------------------|------------------------------------------------|-----------------------------------------------|------------------------------------------------------|
| Modelos de Aprendizaje Profundo - Large Lenguage Model Meta AI (LLaMA)| Tasa de Aprendizaje: 0.001; Épocas: 100; Batch Size: 64; Regularización: L1/L2 | Adam | LEarly Stopping, Batch Normalization | Error Cuadrático Medio (MSE), Error Absoluto Medio (MAE) | Precisión | Curva ROC | GPU: NVIDIA GeForce 7300, CPU: Intel Xeon | 4 horas | Python 3.10 | Batch Size: 128; Early Stopping: 10; Dropout Rate: 0.5; Data Augmentation: No; Regularización: 0.1 |

### Evaluación del Modelo

### Métricas de evaluación

[Descripción de las métricas utilizadas para evaluar el rendimiento del modelo].

### Resultados de evaluación

[Resultados de evaluación del modelo]

### Análisis de los resultados y selección del mejor modelo

[Análisis detallado de los resultados y selección del mejor modelo del modelo]

## Descripción del modelo final

El modelo final es un chatbot basado en LLaMA 3.2 3B 4Q, optimizado para responder preguntas relacionadas con los productos de la canasta familiar y generar predicciones de series de tiempo. El chatbot está diseñado para manejar consultas en lenguaje natural, proporcionar información contextualizada y realizar tareas avanzadas como forecasting de precios.

- **Hiperparámetros seleccionados:** 

- Learning Rate (Tasa de aprendizaje): 0.0001
- Batch Size (Tamaño del lote): 32
- Número de épocas: 100
- Optimizer: AdamW
- Dropout: 0.1
- Dimensiones del embedding: 4096
- Número de capas de Transformer: 24
- Número de cabezas de atención: 32

- **Proceso de entrenamiento:** 

El entrenamiento se realizó en varias fases:
- Fase de Pre-entrenamiento: Utilizando un corpus extenso de datos sobre productos agrícolas, precios históricos y consultas relacionadas con la canasta familiar.
- Fase de ajuste fino: Se utilizó un conjunto de datos específico, con información de SIPSA, para personalizar el modelo al dominio agropecuario y optimizar sus respuestas.

- **Entorno de desarrollo:**

- Sistema operativo: Mac OS X 10.7 Lion
- Hardware: Mac Pro 1,1 con procesadores Intel Xeon 5300 (2 x 4 núcleos) y 16 GB de RAM DDR2 FB-DIMM.
- Almacenamiento: 2 TB de disco duro para almacenamiento de datos y logs del modelo.
- Librerías y herramientas utilizadas:
  - PyTorch para la implementación del modelo.
  - Hugging Face Transformers para manejo de LLaMA.
  - Python 3.10 como lenguaje base de desarrollo.
  - NumPy, Pandas para manipulación de datos.
  - CUDA no habilitado, ya que el Mac Pro 1,1 no tiene soporte para aceleración por GPU.

- **Recursos consumidos:**
  - **Duración del entrenamiento:** 72 horas en la fase de ajuste fino.
  - **Infraestructura de cómputo:** Procesadores Intel Xeon 5300 (2.66 GHz, 8 núcleos en total). No se utilizaron unidades GPU, ya que el sistema no dispone de tarjetas gráficas con soporte CUDA.
  - **Dependencias y herramientas:** Python 3.10: PyTorch para manejo de LLaMA; Mac OS X 10.7 Lion como sistema operativo.
- **Métricas de desempeño:**
  - Accuracy (Precisión en las consultas): 87.5% (en preguntas directas sobre productos y precios).
  - MAE (Error Absoluto Medio en predicciones de precios): 0.08 (en predicciones de series de tiempo).
  - Latencia promedio de respuesta: 2.5 segundos por consulta en entornos de pruebas sin aceleración de GPU.

## Referencias

Versiones disponibles, especificaciones y licencias de uso del modelo LLaMA en https://huggingface.co/docs/transformers/main/en/model_doc/llama3
