from flask import Flask
from flask_bootstrap import Bootstrap
# CSRF Protect
from flask_wtf.csrf import CSRFProtect

# se importa SQLAlchemy ORM
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
bootstrap = Bootstrap()
csrf = CSRFProtect() # csrf protect

# importamos la rutas desde views
from .views import page

# Importar el modelo User
from .models import User

def create_app(config):
    # configuracion del servidor desde un objeto
    app.config.from_object(config)

    # inicializamos el ORM SQLAlchemy
    db.init_app(app)

    # inicializamos la proteccion contra CSRF
    csrf.init_app(app)

    #inicializar bootstrap
    bootstrap.init_app(app)

    # configuramos las rutas de views
    app.register_blueprint(page)

    # se crean las tablas en la base de datos
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app