from flask import Flask         # Importa Flask, el microframework web
from flask_cors import CORS
from routes.product_routes import product_bp  # Importa el Blueprint de productos
from routes.want_products_routes import want_product_bp
#from routes.company_routes import company_bp  # Otro Blueprint (empresas)

app = Flask(__name__)           # Crea una instancia de la app Flask
CORS(app)
# Registrar los endpoints del módulo productos en la ruta /api/products
app.register_blueprint(product_bp, url_prefix="/api/v1/products")
app.register_blueprint(want_product_bp, url_prefix="/api/v1/wants_products")
# Registrar los endpoints del módulo empresas en /api/companies
#app.register_blueprint(company_bp, url_prefix="/api/companies")

if __name__ == "__main__":      # Si ejecutas este archivo directamente...
    app.run(port=8000,debug=True)         # Levanta el servidor en modo debug (te muestra errores, reinicia auto)
