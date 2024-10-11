![dane_sen_logo](https://codeversion.dane.gov.co/OSIS_TestLabExplorers/aulapython/pry-name-yyyy/-/raw/main/assets/images/dane_sen_logo_2024.PNG)

# Informe resumen de modelos

En este resumen abarca la descripción de los algoritmos utilizados, los parámetros ajustados y los resultados obtenidos. El informe detalla el proceso de selección de modelos, las métricas de evaluación empleadas y las conclusiones derivadas de los experimentos, con el propósito de ofrecer una visión comprensiva de cómo los modelos contribuyen a abordar el problema de negocio y las recomendaciones para su posible mejora o implementación.

## Descripción del Problema

[Describir el problema que se buscó resolver con el modelo. Se debe incluir una descripción detallada del problema, el contexto en el que se desarrolla, los objetivos que se persiguen y la justificación del modelo]

## Experimentación

[Indicar los modelos propuestos para abordar el problema de negocio, fundamentados en un análisis del estado del arte]

- Modelo 1: Se plantea el uso del [Nombre del Modelo] que es de tipo [Tipo de modelo] por [Justificación]
- Modelo ...: Se plantea el uso del [Nombre del Modelo] que es de tipo [Tipo de modelo] por [Justificación]
- Modelo n: Se plantea el uso del [Nombre del Modelo] que es de tipo [Tipo de modelo] por [Justificación]

### Variables de entrada

[Indicar el listado de variables de entrada utilizadas en el modelo]

### Variable objetivo

[Indicar cual es la variable objetivo o de estudio utilizada en el modelo]

### Registros de entrenamiento

A continuación se presenta el registro del entrenamiento de los modelos.
 
| **Algoritmo/Modelo Utilizado**                              | **Parámetros de Entrenamiento**                                     | **Técnicas de Optimización**                | **Regularización**                           | **Funciones de Pérdida**                             | **Métricas de Evaluación**                    | **Curvas de Rendimiento**                       | **Configuración de Hardware**                  | **Tiempo de Entrenamiento**                  | **Versiones de Software**                    | **Configuración de Entrenamiento**                   |
|-------------------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------|-----------------------------------------------|--------------------------------------------------|------------------------------------------------|--------------------------------------------------|------------------------------------------------|------------------------------------------------|-----------------------------------------------|------------------------------------------------------|
| Redes Neuronales Convolucionales (CNN), Máquinas de Soporte Vectorial (SVM), Árboles de Decisión, Bosques Aleatorios, Regresión Logística, Redes Neuronales Recurrentes (RNN), K-Nearest Neighbors (KNN), Algoritmos de Ensamble, Modelos de Boosting, Modelos de Aprendizaje Profundo | Tasa de Aprendizaje: 0.001, 0.01, 0.1; Épocas: 10, 50, 100; Batch Size: 16, 32, 64; Regularización: L1/L2 | Adam, SGD, RMSprop, Adagrad, Adadelta, Momentum, Nesterov Accelerated Gradient, Mini-Batch Gradient Descent, Stochastic Gradient Descent, No Optimización | L2, L1, Dropout (0.5), Dropout (0.3), Regularización Lasso, Regularización Ridge, Early Stopping, Data Augmentation, Batch Normalization, No Regularización | Entropía Cruzada, Error Cuadrático Medio (MSE), Error Absoluto Medio (MAE), Hinge Loss, Kullback-Leibler Divergence, Binary Cross-Entropy, Categorical Cross-Entropy, Huber Loss, Mean Squared Logarithmic Error | Precisión, Recall, F1 Score, AUC-ROC, Exactitud, Error Cuadrático Medio (MSE), Error Absoluto Medio (MAE), R^2 Score, Log-Loss, Área Bajo la Curva (AUC) | Curva ROC, Curva PR, Curva de Aprendizaje, Curva de Pérdida, Curva de Precisión, Curva de Recall, Curva de F1 Score, Curva de Exactitud, Curva de MSE, Curva de MAE | GPU: NVIDIA RTX 2080, GPU: NVIDIA Tesla K80, GPU: AMD Radeon RX 580, CPU: Intel Core i7, CPU: AMD Ryzen 7, GPU: NVIDIA GeForce GTX 1080, GPU: NVIDIA RTX 3090, CPU: Intel Xeon, GPU: NVIDIA Tesla V100, GPU: NVIDIA Titan V | 1 hora, 2 horas, 3 horas, 4 horas, 5 horas, 30 minutos, 45 minutos, 2 horas 30 minutos, 3 horas 15 minutos, 4 horas 45 minutos | TensorFlow 2.3, TensorFlow 2.4, PyTorch 1.7, PyTorch 1.8, Scikit-Learn 0.24, Scikit-Learn 1.0, Keras 2.4, Keras 2.5, Python 3.7, Python 3.8 | Batch Size: 32, 64, 128; Early Stopping: 5, 10; Dropout Rate: 0.5, 0.3; Data Augmentation: Sí, No; Regularización: 0.1 |

### Evaluación del Modelo

### Métricas de evaluación

[Descripción de las métricas utilizadas para evaluar el rendimiento del modelo].

### Resultados de evaluación

[Resultados de evaluación del modelo]

### Análisis de los resultados y selección del mejor modelo

[Análisis detallado de los resultados y selección del mejor modelo del modelo]

## Descripción del modelo final

[Descripción detallada del modelo final que se desarrolló para resolver el problema planteado]

Esta descripción puede incluir:
 
- **Hiperparámetros seleccionados:** [listar los hiperparámetros]
- **Proceso de entrenamiento:** [describir el proceso de entrenamiento]
- **Entorno de desarrollo:** [detallar el entorno de desarrollo]
- **Recursos consumidos:**
  - **Duración del entrenamiento:** [indicar el tiempo]
  - **Infraestructura de cómputo:** [detallar la infraestructura utilizada]
  - **Dependencias y herramientas:** [mencionar las herramientas y dependencias empleadas]
- **Métricas de desempeño:** [indicar el resultado de las métricas]
- **Optimización aplicada durante el entrenamiento:** [describir las optimizaciones]

### Conclusiones y Recomendaciones

[Conclusiones y recomendaciones a partir de los resultados obtenidos]

## Referencias

[Referencias utilizadas en el desarrollo del modelo]
