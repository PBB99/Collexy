from flask import Blueprint, request, jsonify
from models.product import new_product, get_product,update_product,delete_product

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
        if not data:
            return jsonify({"error":"Error getting new data"}),200
        NAME = data.get("NAME")
        PRODUCT_TYPE_ID = data.get("PRODUCT_TYPE_ID")
        AMOUNT = data.get("AMOUNT")
        STATUS = data.get("STATUS")
        GRADED = data.get("GRADED")
        PRICE = data.get("PRICE")
        LAST_SOLD_PRICE = data.get("LAST_SOLD_PRICE")
        result=update_product(NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,PRICE,LAST_SOLD_PRICE)
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
        
                # Extracción segura con valores opcionales
        NAME = data.get("NAME")
        PRODUCT_TYPE_ID = data.get("PRODUCT_TYPE_ID")
        AMOUNT = data.get("AMOUNT")
        STATUS = data.get("STATUS")
        GRADED = data.get("GRADED")
        GRADING_COMPANY_ID = data.get("GRADING_COMPANY_ID")
        PRICE = data.get("PRICE")
        LAST_SOLD_PRICE = data.get("LAST_SOLD_PRICE")
        URL = data.get("URL")
        DESCRIPTION = data.get("DESCRIPTION")
        result=new_product(NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION)
        
        return jsonify({"message":result}),201
    except Exception as e:
        return jsonify({
            "error": "Product not inserted",
            "details": str(e)
        }), 500