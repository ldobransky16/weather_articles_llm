# weather_app/utils/language.py

from flask import request
from functools import wraps

SUPPORTED_LANGUAGES = ['en', 'sk']

def get_language():
    """Retrieve the language from request arguments or headers."""
    # Try to get the language from query parameters
    language = request.args.get('language')
    if language and language in SUPPORTED_LANGUAGES:
        return language

    # Fallback to Accept-Language header
    accept_language = request.headers.get('Accept-Language', '')
    if accept_language:
        languages = [lang.split(';')[0] for lang in accept_language.split(',')]
        for lang in languages:
            lang_code = lang.strip()[:2]
            if lang_code in SUPPORTED_LANGUAGES:
                return lang_code

    # Default language
    return 'en'

def require_language(f):
    """Decorator to inject language into the route function."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        language = get_language()
        kwargs['language'] = language
        return f(*args, **kwargs)
    return decorated_function
