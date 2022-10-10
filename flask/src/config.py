from required_env import get_required_envars
from dotenv import load_dotenv
from os import path

# Load dotenv file from the project src directory
dotenv = load_dotenv(path.join(path.join(path.dirname(__file__), ".env")))

# My package to check if required environment variables are defined
# exit(1) if any required environment variables are missing
dbConfig = get_required_envars(
    [
        "POSTGRES_HOST",
        "POSTGRES_PORT",
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_DB",
    ]
)
