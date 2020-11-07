from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap()

# importamos la rutas desde views
from .views import page

def create_app(config):
    # configuracion del servidor desde un objeto
    app.config.from_object(config)

    #inicializar bootstrap
    bootstrap.init_app(app)

    # configuramos las rutas de views
    app.register_blueprint(page)
    return app