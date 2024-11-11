![dane_sen_logo](https://github.com/contreras-juan/pry-sipsa-DANE-f1/blob/main/assets/images/dane_sen_logo_2024.PNG?raw=true)

```
git remote add origin https://codeversion.dane.gov.co/OSIS_TestLabExplorers/aulapython/pry-name-yyyy.git

```

# Proyecto de Ciencia de Datos: SIPSABot DANE - Tu guía de información de la canasta familiar.

## Descripción

Este proyecto de ciencia de datos está diseñado para generar una solución tipo chatbot capaz de responder a las diferentes consultas sobre los productos de la canasta familiar y generar predicciones (forecasting) para series de tiempo definidas por el usuario. El proyecto se enfoca en resolver la necesidad de proporcionar respuestas de forma ágil e intuitiva a las preguntas definidas por el usuario interesado en obtener información específica sobre producción y distribución de productos de la canasta familiar y otros sectores económicos capturados por el SIPSA. Se ejecutó utilizando como lenguaje de programación Python utilizando el servicio de experimentación de Azure Databricks y accediendo a los modelos de Hugging Face Transformers para el modelo LLM y análisis de series temporales. Se espera que al final del proyecto se logre un chatbot funcional que permita realizar consultas interactivas sobre producción y distribución de productos de la canasta familiar y generar predicciones de producción, facilitando la planificación para diferentes actores del sector agropecuario. Este repositorio contiene scripts, notebooks y ejemplos para el preprocesamiento de datos, entrenamiento del modelo LLM, y la implementación de las predicciones, proporcionando una base para la práctica, exploración y mejoras en el análisis de datos.

## Instalación

Para ejecutar este proyecto, sigue los siguientes pasos [Indicar los prerrequisitos para la instalación, los problemas comunes y como resolverlos ]:

### Prerrequisitos

1. **Clona el repositorio** en tu máquina local:
```sh
git clone https://github.com/contreras-juan/pry-sipsa-DANE-f1.git

cd tu_repositorio
```

2. **Crea y activa un entorno virtual** (opcional pero recomendado):
```sh
python3 -m venv <nombre-ambiente-virtual>
source <nombre-ambiente-virtual>/bin/activate # En Windows usa `venv\Scripts\activate`
```

3. **Instala las dependencias** listadas en `requirements.txt`:
```sh
pip install -r requirements.txt
```

4. **Datos**
Este proyecto utiliza datos de [datos.gov.co](https://www.datos.gov.co/), particularmente del sistema de precios de alimentos de Colombia: [https://www.datos.gov.co/Estad-sticas-Nacionales/Sistema-de-Informaci-n-de-Precios-y-Abastecimiento/ugru-ez98/about_data](https://www.datos.gov.co/Estad-sticas-Nacionales/Sistema-de-Informaci-n-de-Precios-y-Abastecimiento/ugru-ez98/about_data)

Para que la aplicación funcione, cree una carpeta de datos:

```sh
mkdir data
```

y descargue ahí todos los .csv del SIPSA. Luego ejecute el cuaderno [0_Data_Processing.ipynb](/notebooks/0_Data_Processing.ipynb)


## Ejecución de la aplicación

```sh
python3 app.py
```