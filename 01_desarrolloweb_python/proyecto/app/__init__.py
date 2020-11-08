from flask import Flask
from flask_bootstrap import Bootstrap
# CSRF Protect
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
bootstrap = Bootstrap()
csrf = CSRFProtect() # csrf protect

# importamos la rutas desde views
from .views import page

def create_app(config):
    # configuracion del servidor desde un objeto
    app.config.from_object(config)

    # inicializamos la proteccion contra CSRF
    csrf.init_app(app)

    #inicializar bootstrap
    bootstrap.init_app(app)

    # configuramos las rutas de views
    app.register_blueprint(page)
    return app