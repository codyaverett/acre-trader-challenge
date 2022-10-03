# Project Creation documentation

Steps used to set up the project.  This document is intended to describe the steps taken to generate the inital Django project.

## Prerequisites

- Install Python 3.10
- Install a recent version of git

## Initial Project setup

```bash
# Create directory for this project
mkdir acre-trader-challenge

# Set current working directory to the new directory
cd acre-trader-challenge

# Set up an isolated pip environment with django 4.1.1 specifically
pipenv install django==4.1.1

# Start using the pipenv context
pipenv shell

# verify django-admin cli tool is set up and working
django-admin

# Verify where pip dependencies are installed
pipenv --venv

# Generate a new django project in root directory
django-admin startproject todos_for_acres .
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

