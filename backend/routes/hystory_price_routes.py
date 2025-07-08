from flask import Blueprint,request,jsonify
from models.hystory_prices import get_history_price

history_price_bp=Blueprint("history",__name__)

@history_price_bp.route("/<int:product_id>",methods={"GET"})
def get_hp_byID(product_id):
    try:
        history_price=get_history_price(product_id)
        if history_price:
            return jsonify(history_price),200
        else:
            return jsonify({
                "message":"Not data found"
            }),404
    except Exception as e:
        return jsonify({
            "error":"Get petition fail",
            "details":str(e)
        }),500