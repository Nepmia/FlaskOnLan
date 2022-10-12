import dotenv
import os

dotenv.load_dotenv()

DJANGO_TOKEN = os.getenv("DJANGO_TOKEN")
DJANGO_ENV = os.getenv("DJANGO_ENV")
