# Acre Trader Coding Challenge

This challenges requirements are for me to build a simple todo api service.

## Project Details
The service should perform CRUD operations on a database of to-do records. The service will be used privately by one user.

A to-do record should consist of the date and time the record was created, the date and time the to-do is due, the date and time the to-do was done, a description of the to-do, and the status of the to-do.

The service should provide valid and appropriate HTTP responses for the type of API resource request.

I am free to use any number of libraries and frameworks that I see fit to use.

### Required
- [x] Create a to-do record by specifying the description and desired date and time of completion.
- [x] Retrieve a list of to-do records.
- [x] Update a to-do record with new values for meaningful fields.
- [x] Delete a to-do record.

### Optional
- [x] Filtering, searching, and sorting to-do records by meaningful fields. (Provided through the Admin panel)
- [x] Implement some level of authentication, whether at the HTTP, app, or some other level.

## Extra
- [x] Create lists of todos so it's not just one big list
- [x] Configured Admin panel with Todos and TodoLists being searchable, and sortable.

## Technologies used
- Python 3
- Django
- Django Rest Framework
- Django Debug Toolbar
- Shell scripts
- Docker
- Postgres database (container)
- Postgres admin (container)

## Development setup

There are only a few steps required before local development can be started on a new machine.

1. Setup a postgres database (I like to use docker)
2. Configure environment variables or create `src/.env`

### Postgres Database
For local development you will need to have docker, Optionally, you can use a basic sqllite db for development.  I'm not using any postgres specific features right now, but I am using postgres to demonstrate my familiarity with containers.

I use the `src/start_db.sh` script to download and run the latest postgres and postgres admin container images. The script also sources from the local `src/.env` file for basic postgres configurations.

### Environment Variable configurations
Certain Environment variables are required for the application to start.  If they aren't defined on the system the Django application will error out.

For local development, you can create a `.env` file in the src directory with the required configurations.

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=postgres
POSTGRES_DB=todo
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

## Tools

- Django Admin - http://127.0.0.1:9000/admin/
- Postgres Admin - http://127.0.0.1:5050/
