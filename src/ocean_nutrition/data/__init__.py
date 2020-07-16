
from ocean_nutrition.data.data import data

def register_app(app):
    app.register_blueprint(data)
    pass
