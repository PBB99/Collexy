from flask import Blueprint, request, jsonify
from models.product import new_product, get_product,update_product,delete_product,get_all_products
from utils.data_sanitizer import DataSanitizer
product_bp = Blueprint("product", __name__)

@product_bp.route("/<int:product_id>", methods=["GET"])
def get_products(product_id):
    try:
        product= get_product(product_id)
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
    
@product_bp.route("/",methods=["PUT"])
def update_product(id):
    try:
        data=request.json()
        clean_data=DataSanitizer.sanitize_payload(data)
        if not data:
            return jsonify({"error":"Error getting new data"}),200

        result=update_product(**clean_data)
        return jsonify({"message":result}),201
    except Exception as e:
        return jsonify({
            "error":"Update petition fail"
        }),500


@product_bp.route("/", methods=["POST"])
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
    
@product_bp.route("/", methods=["GET"])
def getAll_products():
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