
from ocean_nutrition.visualisations.views import views

def register_app(app):
    app.register_blueprint(views)
    pass
