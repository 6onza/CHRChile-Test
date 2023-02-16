## Prueba tecnica para CHRChile

El proyecto esta desarrollado en Django 4.0.1 y Python 3.10.10

## Estaciones de bicis en Santiago
* Esta aplicacion permite ver las estaciones de bicis en Santiago, ademas de ver la cantidad de bicis disponibles en cada una de ellas.
* Se crearon los endpoints para obtener la informacion de las estaciones de bicis como tambien para guardar la informacion en una base de datos.
### Endpoints 
* `/bikes/store-bikes-data/` -> Obtiene la informacion de las estaciones de bicis mediante la API  `http://api.citybik.es` y la guarda en la base de datos.
* `/bikes/bikes-stations/` -> Muestra la informacion de las estaciones de bicis guardadas en la base de datos en una tabla creada con Bootstrap.

## SEIA - Sistema de Evaluación de Impacto Ambiental
* Esta aplicacion permite obtener los proyectos en la pagina de la SEIA, ademas de guardar la información de cada uno de ellos.
* Se creo el script `get_projects.py` utilizando las librerias BeautifulSoup y requests, este realiza un web scraping a la pagina de la SEIA `https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php`
para obtener la informacion de todos los proyectos para luego guardarla en un archivo Json.


### Endpoints
* `/seia-crawler/store-projects/` -> Obtiene la informacion de los proyectos de la SEIA del archivo Json y la guarda en la base de datos.
* `/seia-crawler/projects/` -> Muestra la informacion de los proyectos de la SEIA guardados en la base de datos en una tabla creada con Bootstrap.

## Instalación
* Para instalar el proyecto se debe clonar el repositorio y luego ejecutar el siguiente comando en la carpeta del proyecto:
`pip install -r requirements.txt`
* Se deben configurar las variables de entorno en el archivo `.env` que se encuentra en la carpeta del proyecto, en el archivo `.env.example` se encuentran las variables de entorno que se deben configurar.


## Ejecución
* Para ejecutar el proyecto primero se deben crear las migraciones con el siguiente comando:
`python manage.py makemigrations`
* Luego se deben ejecutar las migraciones con el siguiente comando:
`python manage.py migrate`
* Finalmente se debe ejecutar el servidor con el siguiente comando:
`python manage.py runserver`