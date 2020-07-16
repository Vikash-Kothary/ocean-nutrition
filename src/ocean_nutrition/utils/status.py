from flask import Blueprint, current_app

status = Blueprint('status', __name__)

@status.route('/status')
def ping():
    current_app.logger.error('TODO')
    return 'The service is up.'