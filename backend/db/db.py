# backend/db/connection.py
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv()  # Carga el archivo .env

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            cursor_factory=RealDictCursor
            
        )
        return conn
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        raise
