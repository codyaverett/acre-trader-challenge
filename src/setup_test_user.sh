#!/bin/bash

# We need a test user to run the simple crud scripts.
# I'm a little time constrained right now, so this isn't the most ideal way I'd consider doing this.
# You can follow these instructions or make sure the proper credentials are
# set in `src/toolbox/api_test.py` 
echo "Create test user with password 'testtest'"
python manage.py createsuperuser --username=testuser --email=test@test.com
