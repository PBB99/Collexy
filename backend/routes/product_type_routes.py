from flask import Blueprint,request,jsonify
from models.product_type import *

product_type_bp=Blueprint("ptype",__name__)

#Not sure about how i want to manage this