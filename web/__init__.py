from flask import Flask
from .json_provider import OrjsonProvider

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.json = OrjsonProvider(app)
    
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app