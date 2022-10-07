# Project Design

This document is maintained to list out general project requirements, intents, and project structure.

## Frameworks

### Django
As it was mentioned in the challenge prompt, I chose to use Django as my base application framework to demonstrate use

### DjangoRestFramework
Along with Django, I chose to use the `djangorestframework` to simplify many desirable use cases and patterns.

- User Authentication and permissions
- Serialization of data
- OpenApi Schema generation

## Django Apps

### Todo

- Todo REST API
  - Get a list of todos
  - Create new todo
  - Update an existing todo
  - Delete an existing todo
- Todo List API
  - Get a list of todo lists
  - Create a new list
  - Update an existing list
  - Delete an existing list
  - Add/Remove todos to a todo list (many-to-one)
