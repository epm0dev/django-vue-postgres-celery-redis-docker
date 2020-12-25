django-vue-postgres-project-template
===========
A project template containing a Dockerized Vue.js application that consumes a Django REST API which uses a PostgreSQL database.

## Table of Contents
1. [Acknowledgements](#acknowledgements)
2. [Template Structure](#template-structure)
3. [Using This Template](#using-this-template)
4. [Project Deployment](#project-deployment)

## Acknowledgements
Special thanks to [Very Academy](https://www.youtube.com/channel/UC1mxuk7tuQT2D0qTMgKji3w). Their two Youtube videos ([here](https://www.youtube.com/watch?v=KFO8atMJ4Eg) and [here](https://www.youtube.com/watch?v=iuZViCeW0JM)) helped tremendously in getting the individual backend and frontend components of the project setup and working. Much of the project's boilerplate code is based on [this GitHub repository](https://github.com/veryacademy/YT-Vue-Django-Auth-JWT) of theirs.

Special thanks to [testdriven.io](https://testdriven.io/). This [blog post](https://testdriven.io/blog/django-celery-periodic-tasks/) was very useful when setting up [Celery and Celery Beat](https://docs.celeryproject.org/en/stable/) as well as [redis](https://redis.io/). You can check out the example project referenced in the tutorial [here](https://github.com/testdrivenio/django-celery-beat).

## Template Structure
TODO

## Using This Template
1. To use this template, you'll need to have [Git](https://git-scm.com/downloads/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your computer.
2. Rename the project directory from `django-vue-postgres-project-template` to the name of your project.
3. Change to the project directory and initialize a new git repository from your command line as follows:
   ```
   # Change to the project directory
   cd new-project-directory-name
   
   # Delete the existing .git folder
   rm -rf .git
   
   # Initialize a new git repository for the project
   git init
   ```
4. Build and run the development Docker containers from your command line:
   ```
   # Build and run the development containers
   docker-compose -f docker-compose.dev.yml up -d --build
   ```
5. Make and perform Django database migrations from your command line:
   ```
   # Make database migrations
   docker exec -it api python backend/manage.py makemigrations
   
   # Perform database migrations
   docker exec -it api python backend/manage.py migrate
   ```
6. Create a Django superuser from your command line:
   ```
   # Create new superuser
   docker exec -it api python backend/manage.py createsuperuser
   ```
7. Once the containers are built, you can see what tasks have been run by the celery container from your command line as follows:
   ```
   # Check the celery container logs
   docker-compose -f docker-compose.dev.yml logs celery
   ```

## Project Deployment
Note: These instructions assume that you have already completed the steps provided in the [Using This Template](#using-this-template) section of this README file.
Note: Directions for creating a production environment file are incomplete and will vary drastically depending on how the application is deployed.
1. First, create a new file in the project's root directory called `.env.prd` and, in the newly created file, specify values for the following environment variables:
   ```
   SECRET_KEY=
   ALLOWED_HOSTS=
   POSTGRES_DB=
   POSTGRES_USER=
   POSTGRES_PASSWORD=
   ```
2. Add the following environment variables and their values to the `.env.prd` file you created in the previous step:
   ```
   DEBUG=0
   DB_HOST=production_db
   REDIS_HOST=production_redis
   CORS_ALLOWED_ORIGINS=http://localhost:8000
   ```
3. Stop all running containers and remove their networks, volumes and images from your command line:
   ```
   # Stop any running development containers
   docker-compose -f docker-compose.dev.yml down -v
   
   # Stop any running production containers
   docker-compose -f docker-compose.prd.yml down -v
   ```
4. Build and run the production Docker containers from your command line:
   ```
   # Build and run the production containers
   docker-compose -f docker-compose.prd.yml up -d --build
   ```
5. Make and perform Django database migrations from your command line:
   ```
   # Make database migrations
   docker exec -it production_api python backend/manage.py makemigrations
   
   # Perform database migrations
   docker exec -it production_api python backend/manage.py migrate
   ```
6. Create a Django superuser from your command line:
   ```
   # Create new superuser
   docker exec -it production_api python backend/manage.py createsuperuser
   ```
