from flask import Flask

from ocean_nutrition import data
# from ocean_nutrition import features
# from ocean_nutrition import models
from ocean_nutrition import visualisations
from ocean_nutrition import utils


def create_app():
    app = Flask(__name__)
    app.secret_key = __name__

	# TODO: Use classes to add sections
    data.register_app(app)
    # features.register_app(app)
    # models.register_app(app)
    visualisations.register_app(app)
    utils.register_app(app)
    return app
    

if __name__ == '__main__':
    create_app()
