# TEAM CHALLENGE
[**1. Análisis de los datos proporcionados**](#1-analisis-de-los-datos-proporcionados)\
[**2. Ingesta de datos**](#2-ingesta-de-datos)\
[**3. Implementación de IA generativa**](#3-implementación-de-ia-generativa)\

Para que este proyecto funcione recomendamos crear un entorno virtual e instalar las dependencias a partir de [`requirements.txt`](/requirements.txt)

En los codigos donde se implementan las API, es necesario tener creado un archivo de entorno `.env` siguiendo la plantilla proporcionada [`.env.plantilla`](/.env.plantilla)

### **Datasheets** utilizados en este proyecto
- [movies.csv](./data/movies.csv)
- [links.csv](./data/links.csv)
- [ratings.csv](./data/ratings.csv)
- [tags.csv](./data/tags.csv)

## 1. Análisis de los datos proporcionados

En esta sección se realizarán las comprobaciones y modificaciones nescesarias para un correcto entendimiento y eficiente manipulación de los datos implementandose en el `jupyter notebook` [Organize.ipynb](./Organize.ipynb)

## 2. Ingesta de datos

Valiéndonos de la API de [The Movie DB](https://www.themoviedb.org/) accedemos a las peliculas proporcionadas por `movies.csv` gracias a la columna `movieId` y extraemos datos de relevancia para un mayor entendimiento de la pelicula `overview` y rápida localización `homepage`

## 3. Implementación de IA generativa

Gracias a la API de Gemini somos capaces de traducir la información a el lenguaje nativo de la persona interesada de forma resumida `overveiew_es`

En este caso nos estaremos focalizando en una version reducida de los datos, la cual se puede encontrar en la misma carpeta de `data` bajo el nombre de [movies_with_overview_and_homepage.csv](./data/movies_with_overview_and_homepage.csv)