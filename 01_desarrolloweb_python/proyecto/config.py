class Config:
    SECRET_KEY = 'j5l4kj34jrkf8899*565erre'

class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}