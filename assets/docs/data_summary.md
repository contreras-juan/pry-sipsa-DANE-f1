![dane_sen_logo](https://codeversion.dane.gov.co/OSIS_TestLabExplorers/aulapython/pry-name-yyyy/-/raw/main/assets/images/dane_sen_logo_2024.PNG)


# Informe resumen de datos

El Informe Resumen de Datos ofrece una visión detallada del conjunto de datos utilizado en este proyecto de ciencia de datos. Aquí se describen las principales características del dataset, incluyendo la estructura de las tablas, las variables presentes y las estadísticas descriptivas relevantes. La información contenida en este informe es esencial para comprender los datos y guiar el proceso de modelado y toma de decisiones en el proyecto.

## Resumen general de los datos

A continuación se presenta una visión general detallada del conjunto de datos, incluyendo la descripción de los atributos, su distribución y características estadísticas clave, lo que es fundamental para la fase de análisis exploratorio y la preparación de datos para el modelado.

## Origen de los datos

- [Proporcionar el detalle de la fuente,como se obtuvieron, ubicación y estructura de los archivos de origen de los datos].

| **Fuente**                | **Método de Obtención**                          | **Ubicación**                                  | **Estructura de Datos**                      | **Formato / Extensión**    | **Tamaño**                          | **Versión**                |
|---------------------------|--------------------------------------------------|------------------------------------------------|----------------------------------------------|----------------------------|------------------------------------|----------------------------|
| Plataforma web de Datos Abiertos Colombia (https://www.datos.gov.co)| Extracción directa (Descarga) | Servidor local | Estructurada | CSV | 1.471.928 registros, 10 columnas y  tamaño total DE 0,71 GB | Versión 1.0 |

# Seguridad y Privacidad de Datos

### Requisitos de Seguridad
- **Cifrado de Datos:**
  - No aplica, datos abiertos sin información confidencial.

### Privacidad de Datos
- **Protección de Datos Confidenciales:**
  - No aplica, datos abiertos sin información confidencial.
  
### Consideraciones Éticas
- **Consentimiento y Transparencia:**
- No aplica, datos abiertos sin información confidencial.

### Clasificación de Datos
- **Tipo de Datos:**
  - Descripción: Datos abiertos al público.
  - Relevancia: El conjunto de datos proporciona al modelo una representación rica y diversa del dominio específico que se desea cubrir, en este caso, productos de la canasta familiar, categorias y cantidades. La calidad, cantidad y variedad de los datos permiten al modelo capturar patrones lingüísticos y de contexto necesarios para comprender y responder a consultas complejas de manera coherente y relevante.

### Diccionario de datos

A continuación, se presenta el diccionario de datos, que detalla la estructura del conjunto de datos con descripciones de cada variable, su tipo de dato y los valores posibles. Este sirve como referencia para entender las características y el contenido de los datos utilizados en el proyecto.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| Fuente | Descripción de la variable 1 | Carácter | Sin información | Archivo Nacional de Datos ANDA |
| FechaEncuesta | Fecha en la que se realizo la encuesta | Carácter | Sin información | Archivo Nacional de Datos ANDA |
| Cod. Depto Proc. | Código de la DIVIPOLA del Departamento donde se realizo la encuesta | Carácter | Sin información | Archivo Nacional de Datos ANDA |
| Cod. Municipio Proc. | Código de la DIVIPOLA del Municipio donde se realizo la encuesta | Carácter | Sin información | Archivo Nacional de Datos ANDA |
| Departamento Proc. | Nombre del Departamento donde se realizo la encuesta | Carácter | Sin información | Archivo Nacional de Datos ANDA |
| Municipio Proc. | Nombre del Municipio donde se realizo la encuesta | Carácter | Sin información | Archivo Nacional de Datos ANDA |
| Grupo | Grupo del producto de la canasta de SIPSA | Carácter | Sin información | Archivo Nacional de Datos ANDA |
| Codigo CPC | Códgo de la Clasificación Central de Productos | Carácter | Sin información | Archivo Nacional de Datos ANDA |
| Ali |Nombre del alimento | Carácter | Sin información | Archivo Nacional de Datos ANDA |
| Cant Kg | Cantidad en Kilogramos | Carácter | Sin información | Archivo Nacional de Datos ANDA |

## Movimiento e ingeniería de datos

- Ubicación del origen de los datos: Archivo Nacional de Datos (ANDA) 
- Ubicación del destino de los datos: On-premise WorkStation de Desarrollo
- Métricas de calidad de datos: Sin información
- Reglas de transformación e ingeniería de características a aplicar a los datos.

### Rutinas para la carga de datos

- [Especificar los scripts utilizados para la carga de los datos].