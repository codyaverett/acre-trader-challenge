#!/usr/bin/env python3

# python script to request an api resource and return the response
#
# usage: ./get.py [resource]
#
# example: ./get.py todos

import sys
import requests
import json
from ..api_test import endpoint

# get the resource from the command line
resource = sys.argv[1]

if __name__ == "__main__":
    # make the request
    response = requests.get(f'{endpoint}{resource}/')

    # print the response
    print(json.dumps(response.json(), indent=2))
