import os
from flask import Flask
from . import db, map, localization

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'main.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/test')
    def test():
        return 'Hello, World!'
    
    db.init_app(app)
    app.register_blueprint(map.bp)
    app.register_blueprint(localization.bp)

    return app