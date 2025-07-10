import requests
from dotenv import load_dotenv
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import get_connection
load_dotenv()

def fetch_sets_from_api():
    url="https://api.pokemontcg.io/v2/sets"
    headers = {"X-Api-Key": os.getenv("POKEMON_API_KEY")} 
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Lanza error si la respuesta no es 200
    return response.json()["data"]

def insert_sets_into_db(sets):
    conn = get_connection()
    cursor = conn.cursor()

    for s in sets:
        cursor.execute("""
            INSERT INTO sets (id, name, series, printed_total, total, release_date, logo_url, symbol_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (
            s["id"],
            s["name"],
            s.get("series"),
            s.get("printedTotal"),
            s.get("total"),
            s.get("releaseDate"),
            s["images"]["logo"],
            s["images"]["symbol"]
        ))

    conn.commit()
    cursor.close()
    conn.close()


def sync_sets():
    sets = fetch_sets_from_api()
    insert_sets_into_db(sets)


if __name__ == "__main__":
    sync_sets()
