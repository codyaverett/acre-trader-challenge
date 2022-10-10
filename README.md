# Django Todo REST service

This is a Django REST api project that can be used to create and manage Todos and Lists of Todos.

## Table of Contents

- [Django Todo REST service](#django-todo-rest-service)
  - [Table of Contents](#table-of-contents)
  - [Project Details](#project-details)
  - [Technologies used](#technologies-used)
  - [Features](#features)
    - [Extra features](#extra-features)
  - [Public API](#public-api)
  - [Development](#development)
    - [1. Install Application dependencies](#1-install-application-dependencies)
    - [2. Configure Project Environment Variables](#2-configure-project-environment-variables)
    - [3. Setup a Postgres Database](#3-setup-a-postgres-database)
    - [5. Start the Django development server](#5-start-the-django-development-server)
    - [6. Use the api and development tools](#6-use-the-api-and-development-tools)

## Project Details
The service should perform CRUD operations on a database of to-do records. The service will be used privately by one user.

A to-do record should consist of the date and time the record was created, the date and time the to-do is due, the date and time the to-do was done, a description of the to-do, and the status of the to-do.

The service should provide valid and appropriate HTTP responses for the type of API resource request.

I am free to use any number of libraries and frameworks that I see fit to use.

## Technologies used

- [Python 3](https://docs.python.org/3/index.html)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [Django 4.1](https://docs.djangoproject.com/en/4.1/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar)
- [django_extensions](https://django-extensions.readthedocs.io/en/latest/)
- [Shell scripts](https://en.wikipedia.org/wiki/Shell_script)
- [Docker](https://docs.docker.com/)
- [PostgreSQL database](https://www.postgresql.org/) (container)
- [pgAdmin](https://www.pgadmin.org/) (container)


## Features

- [x] Create a to-do record by specifying the description and desired date and time of completion.
- [x] Retrieve a list of to-do records.
- [x] Update a to-do record with new values for meaningful fields.
- [x] Delete a to-do record.
- [x] Filtering, searching, and sorting to-do records by meaningful fields. (Provided through Admin panel)
- [x] Implements http authentication layer to protect the api from unauthorized write access

### Extra features

- [x] Create lists of todos so it's not just one big list
- [x] Admin panel is configured to allow users to manage their Todos and TodoLists 
- [x] Todos and TodoLists are searchable, and sortable by meaningful fields.

## Public API

```shell
» ./manage.py show_urls | grep /api/v1/ | awk '{ print $1 }'

/api/v1/
/api/v1/\.<format>/
/api/v1/api-auth/login/
/api/v1/api-auth/logout/
/api/v1/todolists/
/api/v1/todolists/<id>/
/api/v1/todolists/<id>\.<format>/
/api/v1/todolists\.<format>/
/api/v1/todos/
/api/v1/todos/<id>/
/api/v1/todos/<id>\.<format>/
/api/v1/todos\.<format>/
/docs/
/docs/schema.js
```

After development setup, view the interactive docs for more detail.
http://127.0.0.1:9001/docs/

## Development

There a few steps required before local development can be started on a new machine.

### 1. Install Application dependencies

Install `pipenv` if you don't already have it.
```shell
pip install --user pipenv
```

Then run `pipenv install --dev` anywhere in the project directory to install all the project dependencies and development dependencies.

### 2. Configure Project Environment Variables

Create a `src/.env` file with the following values:

```ini
POSTGRES_USER=admin
POSTGRES_PASSWORD=postgres
POSTGRES_DB=todo
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### 3. Setup a Postgres Database

Install [docker](https://docs.docker.com/get-docker/) if you don't have it.

With docker installed, run the `src/start_db.sh` script to download and start a `postgres database` and `postgres admin` container images. 

This `src/start_db.sh` script also sources from the `src/.env` file we created for basic postgres configurations.

### 5. Start the Django development server

From the `src/` directory run either:
- the `./start_app.sh` script to start the Django development server on `port 9001`.
- or use `./manage.py runserver 9001`

### 6. Use the api and development tools

- Browsable Api - http://127.0.0.1:9001/api/v1
- Interactive Api Docs - http://127.0.0.1:9001/docs/
- Django Admin - http://127.0.0.1:9001/admin/
- Postgres Admin - http://127.0.0.1:5050/
- [django_extensions](https://django-extensions.readthedocs.io/en/latest/) features are available through the `src/.manage.py` cli
