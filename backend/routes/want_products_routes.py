from flask import Blueprint, request, jsonify
from models.my_wants_products import *
from utils.data_sanitizer import DataSanitizer
want_product_bp = Blueprint("want_product", __name__)

@want_product_bp.route("/<int:wanted_product_id>", methods=["GET"])
def get_wanted_product(wanted_product_id):
    try:
        product= get_product(wanted_product_id)
        if product:
            return jsonify(product),200
        else:
            return jsonify({
                "error":"Product not found"
            }),404
    except Exception as e:
        return jsonify({
            "error": "Get product action fail",
            "details": str(e)
        }), 500
    
@want_product_bp.route("/<int:wanted_product_id>",methods=["PUT"])
def update_petition_product(wanted_product_id):
    try:
        data=request.get_json()
        
        if not data:
            return jsonify({
                "error":"No input data provided"
            }),400
        
        clean_data=DataSanitizer.sanitize_payload(data)
        allowed_keys = ["AMOUNT", "STATUS", "GRADED", "PRICE", "LAST_SOLD_PRICE"]
        filtered_data = {k: clean_data[k] for k in allowed_keys if k in clean_data}
        filtered_data["wanted_product_id"]=wanted_product_id
        

        result=update_product(**filtered_data)
        return jsonify({"message":result}),201
    except Exception as e:
        return jsonify({
            "error":"Update petition fail"
        }),500


@want_product_bp.route("/", methods=["POST"])
def create_product():
    try:
        data=request.get_json()
        required_fields=["NAME", "PRODUCT_TYPE_ID", "AMOUNT", "STATUS", "GRADED"]
        missing_fields=[field for field in required_fields if field not in data or data[field] in [None,""]]

        if missing_fields:
            return jsonify({
                "error":"Required fields missing",
                "missing":missing_fields
            }),400
        
        clean_data=DataSanitizer.sanitize_payload(data)
        result=new_product(**clean_data)
        
        return jsonify({"message":result}),201
    except Exception as e:
        return jsonify({
            "error": "Product not inserted",
            "details": str(e)
        }), 500
    
@want_product_bp.route("/", methods=["GET"])
def getAll_wanted_products():
    try:
        products = get_all_products()  
        if products:
            return jsonify(products), 200
        else:
            return jsonify({"message": "No products found"}), 404
    except Exception as e:
        return jsonify({
            "error": "Get all products failed",
            "details": str(e)
        }), 500

@want_product_bp.route("/<int:want_product_id>",methods={"DELETE"})
def delete_rt_product(want_product_id):
    try:
        deleted_product=delete_product(want_product_id)
        if deleted_product is True:
            return jsonify({
                "message":"Not product deleted"
            }),404     
        return jsonify({"message":"product deleted"}),200
    except Exception as e:
        return jsonify({
            "error": "Delete failed",
            "details": str(e)
        }), 500