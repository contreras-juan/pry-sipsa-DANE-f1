![dane_sen_logo](https://github.com/contreras-juan/pry-sipsa-DANE-f1/blob/main/assets/images/dane_sen_logo_2024.PNG?raw=true)

# Informe resumen de despliegue

Este informe ofrece documenta las estrategias y metodologías empleadas para llevar los modelos desde el entorno de desarrollo hasta el entorno de producción, incluyendo la infraestructura utilizada, los pasos de implementación, y las consideraciones para la integración con sistemas existentes.

### 1. Detalles del Modelo

- **Nombre del Modelo:** Large Language Model Meta AI 
- **Descripción del Modelo:** Large Language Model Meta AI versión 3.2. con  3 mil millones de parámetros y cuantización a 4 bits.

### 2. Plataforma de Despliegue

- **Plataforma de Despliegue:** On-premise
- **Entorno de Despliegue:** Servidor local

### 3. Requisitos Técnicos

- **Versiones de Software:**
  - **Python:** [Versión 3.10.]
  - **Bibliotecas de Terceros:** [Pytorch]
  - **Hardware Requerido:** [Especificaciones de Hardware, e.g., CPU, RAM, GPU]

### 4. Código de Despliegue

- **Archivo Principal de Despliegue:** [Nombre del Archivo, e.g., deploy_model.py]
- **Rutas de Acceso a los Archivos:** [Lista de Rutas de Acceso, e.g., /path/to/config.yaml, /path/to/model.pkl]
- **Variables de Entorno:** [Lista de Variables de Entorno, e.g., `MODEL_PATH`, `DATABASE_URL`]

### 5. Documentación del Despliegue

A continuación, se proporcionan las instrucciones detalladas para la instalación, configuración, uso y mantenimiento del modelo en el entorno de producción.

- **Instalación:** 

[Proporcionar las instrucciones detalladas para instalar el modelo en la plataforma de despliegue]

_Ejemplo:_

1. Clonar el repositorio:

```sh
git clone https://github.com/usuario/repositorio.git
```
2. Crear y activar un entorno virtual, e instalar las dependencias

```sh
python3 -m venv env && source env/bin/activate && pip install -r requirements.txt
```
- **Instrucciones de Configuración:** 

[Proporcionar las instrucciones detalladas para configurar el modelo en la plataforma de despliegue]

_Ejemplo:_

1. Configurar variables de entorno en el archivo '.env':

```sh
MODEL_PATH=/path/to/model.pkl
DATABASE_URL=db.example.com
```
2. Establecer parámetros en 'config.yaml':

```yaml
model:
    path: /path/to/model.pkl
database:
    url: db.example.com
```
- **Instrucciones de Uso:**

[Proporcionar las instrucciones para utilizar el modelo en la plataforma de despliegue]

_Ejemplo:_

1. Ejecutar el script principal para iniciar el servicio de predicción:

```sh
python deploy_model.py
```

2. Comprobar el estado del servicio:

```sh 
curl http://localhost:8080/status
```

- **Instrucciones de Mantenimiento:** 

[Proporcionar las instrucciones detalladas para mantener el modelo en la plataforma de despliegue]

_Ejemplo:_

1. Monitorear logs y métricas de rendimiento:

```sh
tail -f /var/log/model_logs.log
```

2. Actualizar el modelo periódicamente con nuevos datos:

```sh
python update_model.py --data /path/to/new/data
```