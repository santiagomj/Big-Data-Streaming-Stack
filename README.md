# Big Data Streaming Stack

![Example](./docs/stak_bigdata_arq.svg)

Big Data Streaming Stack es un conjunto de tecnologías unificadas con Docker Compose cuyo
proposito es facilitar el aprendizaje de algunas tecnologías como Delta Lake en modo on-premise.

## Dependencias
- Docker 20.10.7
- Docker Compose 1.29.2   

**Nota**: Se recomienda usar docker en alguna distribución de linux para mayor agilidad al momento
de instalar el stack.

## Inicio Rápido

Clonar o descargar el repositorio:

`git clone https://github.com/santiagomj/Big-Data-Streaming-Stack.git`

Acceder por consola o algún ambiente de desarrollo a la carpeta donde fue descargado 
el repositorio y ejecutar docker compose:

`docker-compose up`

Creación de usuario Apache Superset

`docker exec -it superset superset-init`

## Servicios locales

- Control Center: <http://localhost:9021>
- Jupyter Notebook: <http://localhost:8888>
- Hue: <http://localhost:8889>
- Superset: <http://localhost:8088>
- Minio: <http://localhost:9001>

**IMPORTANTE**: Para encontrar la IP en la que está ejecutandose Minio, se debe ir a los logs del contenedor.
