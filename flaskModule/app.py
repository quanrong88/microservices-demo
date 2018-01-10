from flask import Flask, Blueprint
from restplus import api
from services.user import ns as user_namespace
from services.movies import ns as movies_namespace
from services.bookings import ns as bookings_namespace

app = Flask(__name__)

def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)
    api.add_namespace(user_namespace)
    api.add_namespace(movies_namespace)
    api.add_namespace(bookings_namespace)


def main():
    initialize_app(app)
    app.run(host="0.0.0.0", debug=True)

if __name__ == "__main__":
    main()
