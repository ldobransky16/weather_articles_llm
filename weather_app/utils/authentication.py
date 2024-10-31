from flask import request, current_app
from functools import wraps

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key and api_key == current_app.config['API_KEY']:
            return f(*args, **kwargs)
        else:
            return {'error': 'Unauthorized'}, 401
    return decorated
