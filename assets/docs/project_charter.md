![dane_sen_logo](https://codeversion.dane.gov.co/OSIS_TestLabExplorers/aulapython/pry-name-yyyy/-/raw/main/assets/images/dane_sen_logo_2024.PNG)

# Documento marco 

## Nombre del Proyecto

SIPSABot DANE - Tu guía de información de la canasta familiar

## Objetivo del Proyecto

Generar una solución tipo chatbot capaz de responder a las diferentes consultas sobre producción, abastecimiento y disponibilidad de los productos de la canasta familiar y generar predicciones (forecasting) para series de tiempo definidas por el usuario. El proyecto se enfoca en resolver la necesidad de proporcionar respuestas de forma ágil e intuitiva a las preguntas definidas por el usuario interesado en obtener información específica sobre producción y distribución de productos de la canasta familiar y otros sectores económicos capturados por el SIPSA.

## Alcance del Proyecto

### Incluye:

- **Descripción de los datos disponibles**: El conjunto de datos corresponde a la información recolectada por el SIPSA para el periodo de los dos primeros cuatrimestres de 2024, que cubre la oferta y abastecimiento de alimentos en diferentes regiones de Colombia. Las columnas incluidas en el dataset detallan aspectos clave relacionados con las fuentes de información, fechas de encuesta, ubicaciones geográficas y productos. Se encuentra disponible de manera abierta y pública en la plataforma de Datos Abiertos Colombia (https://microdatos.dane.gov.co/index.php/catalog/697/get-microdata).

-**Descripción de los resultados esperados**: Se espera contar con una solución tipo chatbot capaz de responder a las diferentes consultas sobre los productos de la canasta familiar y generar predicciones (forecasting) para series de tiempo definidas por el usuario.

-**Criterios de éxito del proyecto**: La solución chatbot debe ser capaz de proporcionar respuestas precisas sobre productos de la canasta familiar, incluyendo consultas sobre procedencia departamental, municipal, cantidades y categorías, con un 90% de precisión en las respuestas textuales.

### Excluye:

- Descripción detallada de los hiper parámetros del modelo.

## Arquitectura de la solución

En esta sección, presentamos la arquitectura general del proyecto, la cual ha sido diseñada para optimizar el flujo de trabajo y alcanzar los objetivos del proyecto. La arquitectura está integrada por los siguientes componentes [_Indicar solo los que se requieran_]:

- **Herramientas de gestión y almacenamiento de datos:** Para la gestión y almacenamiento de datos utilizamos la base de datos estructurada de Oracle.
 
- **Herramientas de desarrollo y entrenamiento de modelos:** Para el desarrollo y entrenamiento de modelos, usamos la biblioteca de ciencia de datos de Python denominada Transformers.
 
- **Herramientas de MLOps y CI/CD:** Para MLOps y CI/CD, utilizamos integración continua, despliegue continuo, operación y mantenimiento de modelos y versionado de código con GitHub.
 
## Metodología

[Descripción breve de la metodología que se utilizará para llevar a cabo el proyecto]

## Cronograma

| Proceso clave | Duración Estimada | Fechas |
|------|---------|-------|
| Iniciación del proyecto | 2 semanas | del 1 de Agosto al 15 de Agosto |
| Ingeniería de características | 2 semanas | del 16 de Agosto al 31 de Agosto |
| Experimentación | 4 semanas | del 1 de Septiembre al 30 de Septiembre |
| Pipeline del flujo de trabajo automatizado de ciencia de datos | 4 semanas | del 1 de Octubre al 31 de Octubre |

## Equipo del Proyecto

- **Juan Felipe Contreras Alcivar](https://github.com/contreras-juan)** - *Rol principal* - Científico de datos a cargo del desarrollo de los modelos.
- **Alejandro Sandoval Pineda (https://github.com/alsandovalp)** - *Rol secundario* - Líder del proyecto de ciencia de datos.

## Aprobaciones

- Alejandro Sandoval Pineda - Líder del proyecto de ciencia de datos
- Fecha de aprobación: 15/10/2024

## Resumen Ejecutivo

Describe los resultados del proyecto de ciencia de datos y presenta los principales logros y lecciones aprendidas durante el proceso.

## Resultados del proyecto

- Resumen de los entregables y logros alcanzados en cada etapa del proyecto.
- Evaluación del modelo final y comparación con el modelo base.
- Descripción de los resultados y su relevancia para el negocio.

## Lecciones aprendidas

- Identificación de los principales desafíos y obstáculos encontrados durante el proyecto.
- Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo.
- Recomendaciones para futuros proyectos de machine learning.

## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria.
- Identificación de las áreas de mejora y oportunidades de desarrollo futuras.

## Conclusiones

- Resumen de los resultados y principales logros del proyecto.
- Conclusiones finales y recomendaciones para futuros proyectos.
