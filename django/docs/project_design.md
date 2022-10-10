# Project Design

This document is maintained to list out general project requirements, intents, tools, and project structure.

## Table of contents
- [Project Design](#project-design)
  - [Table of contents](#table-of-contents)
  - [Frameworks](#frameworks)
    - [Django](#django)
    - [DjangoRestFramework](#djangorestframework)
  - [Django Apps](#django-apps)
    - [Todo_app](#todo_app)

## Frameworks

### Django
I chose to use Django as my base application framework to demonstrate use

### DjangoRestFramework
Along with Django, I chose to use the `djangorestframework` to simplify many desirable use cases and patterns for this challenge.

- User Authentication and permissions
- Serialization of data
- OpenApi Schema generation

It doesn't take much to get a fully functional todo application with this toolset.

## Django Apps

### Todo_app

The primary application for this demo.

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
