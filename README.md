# Acre Trader Coding Challenge

This challenges requirements are for me to build a simple todo api service.

## Project Details
The service should perform CRUD operations on a database of to-do records. The service will be used privately by one user.

A to-do record should consist of the date and time the record was created, the date and time the to-do is due, the date and time the to-do was done, a description of the to-do, and the status of the to-do.

The service should provide valid and appropriate HTTP responses for the type of API resource request.

I am free to use any number of libraries and frameworks that I see fit to use.

### Required
- [ ] Create a to-do record by specifying the description and desired date and time of completion.
- [ ] Retrieve a list of to-do records.
- [ ] Update a to-do record with new values for meaningful fields.
- [ ] Delete a to-do record.

### Optional
- [ ] Filtering, searching, and sorting to-do records by meaningful fields.
- [ ] Implement some level of authentication, whether at the HTTP, app, or some other level.

## Technologies used
- Python 3
- Django
- Django Rest Framework
- Shell scripting
- Docker
- Postgres database (container)
- Postgres admin (container)

## Development setup

There are only a few steps required before local development can be started on a new machine.

1. Setup a postgres database (I like to use docker)
2. Configure environment variables or create `src/.env`

### Postgres Database
For local development you will need to have docker, Optionally, you can use a basic sqllite db for development.  I'm not using any postgres specific features right now, but I am using postgres to demonstrate my familiarity with containers.

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
