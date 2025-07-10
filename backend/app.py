from flask import *       # Importa Flask, el microframework web
from flask_cors import CORS
from routes.product_routes import product_bp  # Importa el Blueprint de productos
from routes.want_products_routes import want_product_bp
from routes.hystory_price_routes import history_price_bp
from routes.scraper_routes import scraper_bp


app = Flask(__name__)           # Crea una instancia de la app Flask
CORS(app)

app.register_blueprint(product_bp, url_prefix="/api/v1/products")
app.register_blueprint(want_product_bp, url_prefix="/api/v1/wants_products")
app.register_blueprint(history_price_bp, url_prefix="/api/v1/history")
app.register_blueprint(scraper_bp, url_prefix="/api/v1/scraper")



if __name__ == "__main__":      
    app.run(port=8000,debug=True)         