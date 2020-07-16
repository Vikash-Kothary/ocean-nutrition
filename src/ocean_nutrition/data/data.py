
import os
import myfitnesspal
import openfoodfacts
from flask import Blueprint, session
from datetime import datetime


username = os.getenv('MYFITNESSPAL_USERNAME')
password = os.getenv('MYFITNESSPAL_PASSWORD')
client = myfitnesspal.Client(username, password=password)

data = Blueprint('data', __name__)

@data.route('/search/<barcode>')
def search(barcode):
    response = dict()
    response['barcode'] = int(barcode)
    
    ## TODO: Check cache

    # Get from OpenFoodFacts
    product = openfoodfacts.products.get_product(barcode)
    if product['status_verbose'] != 'product found':
        return response

    response['product_name'] = product['product']['product_name']
    if not response['product_name']:
        response['product_name'] = product['product']['product_name_fr']

    if 'brands' in product['product']:
        response['product_brand'] = product['product']['brands']
    else:
        response['product_brand'] = ''

    # TODO: Get from myfitnesspal
    results = client.get_food_search_results(f"{response['product_brand']} {response['product_name']}")
    match = results[0]
    response['verified'] = match.verified
    response['id'] = match.mfp_id
    response['brand'] = match.brand
    response['name'] = match.name
    response['unit'] = 'g'
    response['quantity'] = 100
    response['calories'] = int(match.details["energy"]["value"])
    response['protein'] = match.details["protein"]
    response['fat'] = match.details["fat"]
    response['carbohydrates'] = match.details["carbohydrates"]
    response['fiber'] = match.details["fiber"]
    response['sugar'] = match.details["sugar"]

    response['calorie_density'] = response['calories'] / response['quantity']


    return response


@data.route('/tracker')
def tracker():
    response = dict()
    response['today'] = datetime.today().strftime('%Y-%m-%d')
    
    day = client.get_date(*response['today'].split('-'))
    response['total_calories'] = int(day.totals['calories'])

    response['total_quantity'] = 0
    for meal in day.meals:
        for entry in meal.entries:
            if entry.unit == 'g' or entry.unit == 'serving(s)':
                response['total_quantity'] += int(entry.quantity)
            else:
                response['error'] = f'Uses non-standard unit: {entry.unit}'
                return response

    if not response['total_quantity'] > 0:
        response['error'] = f'Total quantity is zero'
        return response
    response['average_calorie_density'] = response['total_calories'] / response['total_quantity']

    return response
