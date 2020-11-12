class Config:
    SECRET_KEY = 'j5l4kj34jrkf8899*565erre'

class DevelopmentConfig(Config):
    DEBUG = True
    #SQLAlchemy_DATABASE_URI = 'GESTOR://USUARIO:CONTRASEÑA@DIRECCION/NOMBRE_BASE_DE_DATO'
    SQLALCHEMY_DATABASE_URI = 'mysql://userdb:cmfFPWvBNDrjwgyV@127.0.0.1:8888/task_project_python'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}