from flask import Flask

app = Flask(__name__)

# importamos la rutas desde views
from .views import page

def create_app():
    # configuramos las rutas de views
    app.register_blueprint(page)
    return app