from sys import exit
from os import environ


def load_required_envars(required_envars: list) -> dict:
    """ 
    Load required environment variables from .env file
    :param required_envars: list of required environment variables
    :return: dictionary of environment variables
    """
    # Dictionary of parsed environment variables
    envs = {}
    exit_on_complete = False

    for envar in required_envars:
        try:
            envs[envar] = environ[envar]
        except KeyError as key:
            print(f'Please define the environment variable {key}')
            exit_on_complete = True

    if exit_on_complete:
        exit(1)

    return envs
