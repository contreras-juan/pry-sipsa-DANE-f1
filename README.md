![dane_sen_logo](https://codeversion.dane.gov.co/OSIS_TestLabExplorers/aulapython/pry-name-yyyy/-/raw/main/assets/images/dane_sen_logo_2024.PNG)

```
git remote add origin https://codeversion.dane.gov.co/OSIS_TestLabExplorers/aulapython/pry-name-yyyy.git

```

# Proyecto de Ciencia de Datos: SIPSABot DANE - Tu guía de precios de la canasta familiar.

## Descripción

Este proyecto de ciencia de datos está diseñado para generar una solución tipo chatbot capaz de responder a las diferentes consultas sobre los precios de la canasta familiar y generar predicciones (forecasting) para series de tiempo definidas por el usuario. El proyecto se enfoca en resolver la necesidad de proporcionar respuestas de forma ágil e intuitiva a las preguntas definidas por el usuario interesado en obtener información específica sobre los precios y costos de la canasta familiar y otros sectores económicos capturados por el SIPSA. Se ejecutó utilizando como lenguaje de programación Python utilizando el servicio de experimentación de Azure Databricks y accediendo a los modelos de Hugging Face Transformers para el modelo LLM y análisis de series temporales. Se espera que al final del proyecto se logre un chatbot funcional que permita realizar consultas interactivas sobre los precios de la canasta familiar y generar predicciones de precios futuros, facilitando la planificación para diferentes actores del sector agropecuario. Este repositorio contiene scripts, notebooks y ejemplos para el preprocesamiento de datos, entrenamiento del modelo LLM, y la implementación de las predicciones, proporcionando una base para la práctica, exploración y mejoras en el análisis de datos.

## Índice

- [Instalación](#instalación)
- [Uso](#uso)
- [Datos](#datos)
- [Modelos](#modelos)
- [Evaluación](#evaluación)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Autores](#autores)

## Instalación

Para ejecutar este proyecto, sigue los siguientes pasos [Indicar los prerrequisitos para la instalación, los problemas comunes y como resolverlos ]:

### Prerrequisitos

1. **Clona el repositorio** en tu máquina local:
    ```sh
    git clone https://gitlab.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. **Crea y activa un entorno virtual** (opcional pero recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate # En Windows usa `venv\Scripts\activate`
    ```

3. **Instala las dependencias** listadas en `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

### Problemas Comunes

Proporciona una sección para resolver problemas comunes que los usuarios puedan encontrar

## Uso

Debe proporcionar instrucciones claras y detalladas sobre cómo ejecutar y utilizar el proyecto, incluyendo ejemplos y comandos específicos.

**Por ejemplo:**

A continuación se describen los pasos necesarios para utilizar este proyecto después de haber completado la instalación.

### Ejecutar el Script Principal

Para ejecutar el script principal del proyecto, usa el siguiente comando:

```sh
python main.py
```
Si el proyecto incluye una API o una interfaz web, proporciona instrucciones sobre cómo iniciar el servidor y acceder a la interfaz:

```sh
# Iniciar el servidor
python app.py
# Acceder a la interfaz web
http://localhost:5000
```

## Datos

Esta sección describe los conjuntos de datos utilizados en este proyecto, incluyendo cómo obtenerlos y cualquier preprocesamiento necesario.

### Descripción del Conjunto de Datos

Proporciona una breve descripción del conjunto de datos, incluyendo la fuente, el formato y las características principales.

| **Fuente**                                               | **Formato**   | **Descripción**                                           | **Peso (GB)** |
|----------------------------------------------------------|---------------|-----------------------------------------------------------|---------------|
| https://microdatos.dane.gov.co/index.php/catalog/697/get-microdata | CSV | Conjunto de datos del Sistema de Información de Precios y Abastecimiento - SIPSA, el cual analiza el comportamiento de la canasta familiar pero También de sectores como transporte, educación y construcción y empresas. Están disponibles series, índices y variaciones de 10 índices diferentes, así como sistemas de consulta dinámica y metodologías.| 0,71 GB |

### Descargar los Datos

Instrucciones sobre cómo obtener los datos. Esto puede incluir enlaces para descargar archivos o instrucciones para obtener datos de una API.

1. **Descarga el archivo de datos desde https://microdatos.dane.gov.co/index.php/catalog/697/get-microdata**.
2. **Extrae el archivo** (si es necesario) y colócalo en el directorio adecuado:
    ```sh
    mkdir data
    unzip dataset.zip -d data/
    ```
### Preprocesamiento de los Datos

Si es necesario, proporciona detalles sobre cualquier preprocesamiento que debe realizarse en los datos antes de utilizarlos en el análisis o modelado.

```sh
# Script de preprocesamiento (ejemplo)
python preprocess_data.py --input data/raw/reviews.csv --output data/processed/reviews_clean.csv
```
## Modelos

Esta sección describe los modelos utilizados en este proyecto, incluyendo su entrenamiento y uso.

### Descripción de los Modelos

Proporciona una breve descripción de los modelos utilizados y su propósito.

_Ejemplo_: 

- **Modelo de Regresión Logística:** Utilizado para predecir la probabilidad de un evento binario.
- **Modelo de Árbol de Decisión:** Utilizado para la clasificación de categorías múltiples.
- **Modelo de Red Neuronal:** Utilizado para tareas de predicción complejas.

### Entrenamiento de los Modelos

Instrucciones sobre cómo entrenar los modelos con los datos.

```sh
python train_model.py --model decision_tree --input data/processed/reviews_clean.csv --output models/decision_tree_model.pkl
```
### Uso de los Modelos

Proporciona ejemplos de cómo utilizar los modelos entrenados para hacer predicciones

```sh
python predict.py --model models/decision_tree_model.pkl --input data/new_data.csv --output results/predictions.csv
```

## Evaluación

### Métricas de Evaluación

Indica las métricas de evaluación de los modelos

_Ejemplo_:

- **Exactitud (Accuracy):** Proporción de predicciones correctas.
- **Precisión (Precision):** Proporción de verdaderos positivos entre los positivos predichos.
- **Recall (Sensibilidad):** Proporción de verdaderos positivos entre los positivos reales.
- **F1-Score:** Media armónica de precisión y recall.

### Evaluación de los Modelos

Proporciona ejemplos de cómo evaluar los modelos utilizando scripts específicos.

```sh
python evaluate_model.py --model models/logistic_model.pkl --input data/test_data.csv
python evaluate_model.py --model models/decision_tree_model.pkl --input data/test_data.csv
python evaluate_model.py --model models/neural_network_model.h5 --input data/test_data.csv
```

## Contribuciones

Para realizar contribuciones a este proyecto, sigue estos pasos:

1. Realiza un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza los cambios necesarios y realiza commits (`git commit -m 'Añadir nueva característica'`).
4. Envía tus cambios a tu repositorio fork (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request en este repositorio.

### Licencia

Propociona el detalle de la licencia bajo la cual se distribuye tu proyecto.

_Ejemplo:_

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

## Autores
 
Este proyecto ha sido desarrollado por:
 
- **Juan Felipe Contreras Alcivar](https://github.com/contreras-juan)** - *Rol principal* - Científico de datos a cargo del desarrollo de los modelos.
- ** Alejandro Sandoval Pineda (https://github.com/alsandovalp)** - *Rol secundario* - Líder del proyecto de ciencia de datos..
 
Si deseas más información sobre los colaboradores del proyecto, consulta la lista de [colaboradores](https://gitlab.com/tu-repositorio/colaboradores) que participaron en este proyecto.
# pry-sipsa-DANE-f1
