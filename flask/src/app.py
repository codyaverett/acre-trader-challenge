from flask import Flask
from required_env import get_required_envars
from dotenv import load_dotenv

from .config import dbConfig
from .db import Database

app = Flask(__name__)

# configure postgresql connection
conn = Database(
    host=dbConfig["POSTGRES_HOST"],
    database=dbConfig["POSTGRES_DB"],
    user=dbConfig["POSTGRES_USER"],
    password=dbConfig["POSTGRES_PASSWORD"],
    port=dbConfig["POSTGRES_PORT"],
)


@app.route("/")
def root():
    conn.create_table()
    conn.insert("test")
    conn.get_all()
    return "Hello World!"
