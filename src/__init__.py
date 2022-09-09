from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object('config.DevConfig')

    @app.route('/')
    def home():
        return "Hello World"

    return app