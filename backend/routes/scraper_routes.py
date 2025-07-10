from flask import Blueprint, request, jsonify
from scraper.pokemon_tcg_api import get_cards_by_set,search_cards_by_name

scraper_bp = Blueprint("scraper", __name__)
#busqueda de cartas por set, y nombre o sin nombre
@scraper_bp.route("/cards", methods=["GET"])
def fetch_cards():
    set_id = request.args.get("set_id")


    if not set_id:
        return jsonify({"error": "Missing set_id"}), 400

    cards = get_cards_by_set(set_id)
    if cards is None:
        return jsonify({"error": "Failed to retrieve cards"}), 500

    return jsonify(cards), 200

#busqueda de carta por nombre
@scraper_bp.route("/search", methods=["GET"])
def search_cards():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "You must provide a card name"}), 400
    
    cards = search_cards_by_name(name)
    return jsonify(cards), 200

@scraper_bp.route("/test_cards", methods=["GET"])
def test_fetch_cards():
    set_id = request.args.get("set_id")
    if not set_id:
        return jsonify({"error": "Missing set_id"}), 400
    return jsonify({"set_id_received": set_id}), 200