# Proyecto de Gestión de Inventario y transacciones de Blackmounster

## Descripción General

Este proyecto permite la gestión de inventario Blackmounster. El sistema está implementado con Django y utiliza una base de datos PostgreSQL.

## Pasos para la Instalación y Configuración del Entorno

1. **Clonar el Repositorio**

   Clona el repositorio de GitHub:

   ```bash
   git clone https://github.com/lmendozam1983/blackmounster_lmm.git
   cd blackmounster_lmm

2. **Crear y Activar el Entorno Virtual**

    En el directorio del proyecto, crea un entorno virtual para evitar conflictos con las dependencias del sistema:

    ```bash
    mkvirtualenv gestion_inventario
    workon gestion_inventario

3.  **Instalar las Dependencias**

    Instala las dependencias del proyecto desde el archivo requirements.txt:

    ```bash
    pip install -r requirements.txt

## Instalar PostgreSQL

Si aún no tienes PostgreSQL instalado, sigue los pasos en la documentación oficial de PostgreSQL para instalarlo en tu sistema operativo.

## Configurar la Base de Datos

1.  Crea una base de datos para el proyecto. Abre la terminal de PostgreSQL:

     ```bash
    sudo -u postgres psql

2.  Luego, ejecuta los siguientes comandos para crear una base de datos y un usuario:

     ```bash    
    CREATE DATABASE db_blackmounster;
    CREATE USER blackmounster_user WITH PASSWORD 'blackmounster_pass';
    ALTER ROLE blackmounster_userSET client_encoding TO 'utf8';
    ALTER ROLE blackmounster_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE blackmounster_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE gestion_reservas TO blackmounster_user;
    ALTER ROLE blackmounster_user SUPERUSER
    \q

3.  Configurar el archivo **settings.py** en Django

En el archivo settings.py de tu proyecto Django, configura la base de datos PostgreSQL con los datos creados anteriormente:

    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'db_blackmounster',
            'USER': 'blackmounster_user',
            'PASSWORD': 'blackmounster_pass',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

## Instrucciones para Ejecutar el Proyecto y Cargar Datos Iniciales

1.  Migrar la Base de Datos

Ejecuta las migraciones para configurar las tablas de la base de datos:

    
    python3 manage.py makemigrations
    python3 manage.py migrate

2.  Ejecutar el Servidor de Desarrollo

Para ejecutar el servidor de desarrollo de Django, usa el siguiente comando:

    
    python manage.py runserver

## Dependencias del Proyecto

Este proyecto utiliza las siguientes dependencias. Puedes verlas en el archivo requirements.txt y instalarlas con pip:

    
    asgiref==3.8.1
    beautifulsoup4==4.12.3
    crispy-bootstrap5==2024.10
    Django==4.2.18
    django-bootstrap-v5==1.0.11
    django-crispy-forms==2.3
    psycopg==3.2.3
    soupsieve==2.6
    sqlparse==0.5.3
    typing_extensions==4.12.2

Se pueden instalar todas las dependencias usando el archivo requirements.txt, usando el siguinete comando:

    
    pip install -r requirements.txt


## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Creado por LMM.



