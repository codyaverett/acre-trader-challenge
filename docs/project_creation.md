# Project Creation documentation

Steps used to set up the project.  This document is intended to describe the steps taken to generate the inital Django project, setup the database, and super user for administration.

## Prerequisites

- Install Python 3.10
- Install a recent version of git

## Initial Project creation

```bash
# Create directory for this project
mkdir acre-trader-challenge

# Set current working directory to the new directory
cd acre-trader-challenge

# Set up an isolated pip environment with django and djangorestframework
pipenv install django==4.1.1
pipenv install djangorestframework==3.14.0

# Start using the pipenv context
pipenv shell

# verify django-admin cli tool is set up and working
django-admin

# Verify where pip dependencies are installed
pipenv --venv

# Generate a new django project in root directory
django-admin startproject todo_project .
```

## Setup github repository

Created a new public git repository called `codyaverett/acre-trader-challenge`

Commit first files to the repository.

```bash
git add .
git commit -m "initial django project generation"
```

Add the remote repository and push up the code.

```bash
# Adds git remote upstream repository as `origin`
git remote add origin git@github.com:codyaverett/acre-trader-challenge.git

# Move current branch to be `main`
# -M is a Shortcut for --move --force.
git branch -M main

# Push the local main branch to the remote upstream
git push -u origin main
```

## Setup local DB with migrate command
For simplicity of setup I'm using the default sqlite3 db integration.

Running `migrate` will create the initial db file with default values.

```bash
~/Projects/jobs/acre-trader-challenge (main) » python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

## Enabling Super User for administration
Ensure all migration operations have been completed already via `python3 manage.py migrate`

```bash
~/Projects/jobs/acre-trader-challenge (main) » python manage.py createsuperuser
Username (leave blank to use 'caavere'): 
Email address: codyaverett@gmail.com
Password: 
Password (again): 
Superuser created successfully.
```

## Viewing the local sqlite db
Having the sqlite3 binary installed will let you use the CLI client interface to configure and query the local db.

```shell
~/Projects/jobs/acre-trader-challenge (main) » sqlite3 db.sqlite3
sqlite> .tables
auth_group                  auth_user_user_permissions
auth_group_permissions      django_admin_log          
auth_permission             django_content_type       
auth_user                   django_migrations         
auth_user_groups            django_session   
```

## Run the project server
I like to start the development server on port 9000. 

```shell
~/Projects/jobs/acre-trader-challenge (main*) » python3 manage.py runserver 9000

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 05, 2022 - 20:21:04
Django version 4.1.1, using settings 'todo_project.settings'
Starting development server at http://127.0.0.1:9000/
Quit the server with CONTROL-C.
```

- Verify the app is running at [http://127.0.0.1:9000/](http://127.0.0.1:9000/)
- Verify the super user login works through [http://127.0.0.1:9000/admin/](http://127.0.0.1:9000/admin/)

If those both work, then you are good to go.
