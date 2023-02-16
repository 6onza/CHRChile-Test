## Prueba tecnica para CHRChile

Este es un proyecto desarrollado en Django 4.0.1 y Python 3.10.10 que cuenta con dos aplicaciones: una para visualizar y almacenar la información de las estaciones de bicicletas en Santiago y otra para obtener y almacenar información de proyectos del Sistema de Evaluación de Impacto Ambiental (SEIA).

## Estaciones de bicis en Santiago
Esta aplicación permite visualizar las estaciones de bicicletas en Santiago y la cantidad de bicicletas disponibles en cada una de ellas. Se crearon vistas para acceder a la información de las estaciones y guardar la información en una base de datos.
### Endpoints
* `/bikes/store-bikes-stations-data/` -> Obtiene la informacion de las estaciones de bicis mediante la API  `http://api.citybik.es` y la guarda en la base de datos.
* `/bikes/bikes-stations/` -> Muestra la informacion de las estaciones de bicis guardadas en la base de datos en una tabla creada con Bootstrap.

## SEIA - Sistema de Evaluación de Impacto Ambiental
Esta aplicación permite obtener información de proyectos en la página del SEIA y almacenar la información de cada uno de ellos. Se creó un script get_projects.py utilizando las librerías BeautifulSoup y requests para obtener la información de todos los proyectos y guardarla en un archivo JSON.


### Endpoints
* `/seia-crawler/store-projects-data/` -> Obtiene la informacion de los proyectos de la SEIA del archivo Json y la guarda en la base de datos.
* `/seia-crawler/projects/` -> Muestra la informacion de los proyectos de la SEIA guardados en la base de datos en una tabla creada con Bootstrap.

## Instalación
* Para instalar el proyecto se debe clonar el repositorio y luego ejecutar el siguiente comando en la carpeta del proyecto:
`pip install -r requirements.txt`
* Se deben configurar las variables de entorno en el archivo `.env` que se encuentra en la carpeta del proyecto, en el archivo `.env.example` se encuentran las variables de entorno que se deben configurar.


## Migraciones
* Para ejecutar el proyecto primero se deben crear las migraciones con el siguiente comando:
`python manage.py makemigrations`
* Luego se deben ejecutar las migraciones con el siguiente comando:
`python manage.py migrate`


## Ejecución 
* Ejecutar el servidor con el comando: `python manage.py runserver`
* Luego, se puede acceder a los endpoints mencionados anteriormente.

#### Se crearon las vistas en el administrador `/admin/` para visualizar la información almacenada en los modelos de ambas aplicaciones.
