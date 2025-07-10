import requests
from dotenv import load_dotenv
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import get_connection
load_dotenv()
BASE_URL = "https://api.pokemontcg.io/v2/cards"
HEADERS = {
    "Accept": "application/json",
    "X-Api-Key": os.getenv("POKEMON_API_KEY") 
}

def get_cards_by_set(set_id):
    try:
        query = f"set.id:{set_id}"

        response = requests.get(
            f"{BASE_URL}?q={query}",
            headers=HEADERS
        )
        response.raise_for_status()

        cards = response.json()["data"]
        return cards

    except requests.exceptions.RequestException as e:
        print("Error fetching cards:", e)
        return None


def search_cards_by_name(name: str, page=1, page_size=10):
    try:
        params = {
            "q": f'name:"{name}"',
            "page": page,
            "pageSize": page_size
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")

        data = response.json()
        return data.get("data", [])

    except Exception as e:
        print("Error during Pokémon card search:", e)
        return []