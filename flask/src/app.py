from os import path, environ
from flask import Flask
from required_env import get_required_envars
from dotenv import load_dotenv
import psycopg2

app = Flask(__name__)

# Load dotenv file from the project src directory
dotenv = load_dotenv(path.join(path.join(path.dirname(__file__), ".env")))

required_envars = get_required_envars(
    [
        "POSTGRES_HOST",
        "POSTGRES_PORT",
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_DB",
    ]
)

## configure postgresql connection
# conn = psycopg2.connect(
#     host=required_envars["POSTGRES_HOST"],
#     database=required_envars("POSTGRES_DB"),
#     user=required_envars("POSTGRES_USER"),
#     password=required_envars("POSTGRES_PASSWORD"),
#     port=required_envars("POSTGRES_PORT"),
# )


@app.route("/")
def root():
    return "Hello World!"
