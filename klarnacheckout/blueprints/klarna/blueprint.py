from flask import Blueprint
from klarnacheckout.blueprints.klarna import views

# Instantiate a blueprint object
klarna_blueprint = Blueprint('klarna', __name__, url_prefix='/klarna')

# Add URL rules
klarna_blueprint.add_url_rule('/checkout/', view_func=views.Checkout.as_view('checkout'))
klarna_blueprint.add_url_rule('/confirmation/', view_func=views.Confirmation.as_view('confirmation'))