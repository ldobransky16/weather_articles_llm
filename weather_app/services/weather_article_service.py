# weather_app/services/weather_article_service.py
import random
import requests
from flask import current_app
from datetime import datetime
from weather_app.utils.openai_helper import generate_article_text


def generate_weather_article(latitude, longitude, date, language='en'):
    api_key = current_app.config['WEATHER_API_KEY']
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'lat': latitude,
        'lon': longitude,
        'units': 'metric',
        'appid': api_key,
    }
    try:
        today = datetime.utcnow().date()
        if date != today:
            weather_data = generate_mock_weather_data(latitude, longitude)
        else :
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            weather_data = response.json()

        mode = "catastrophic"
        mode_2 = "sensational"
        article_content = generate_article_text(weather_data, language, mode, date)
        article_content_2 = generate_article_text(weather_data, language, mode_2, date)

        result = {
            'location': {
                'name': weather_data.get('name', ''),
                'country': weather_data['sys'].get('country', ''),
                'coordinates': {
                    'latitude': weather_data['coord']['lat'],
                    'longitude': weather_data['coord']['lon']
                },
            },
            'weather': {
                'description': weather_data['weather'][0]['description'],
                'temperature': weather_data['main']['temp'],
                'humidity': weather_data['main']['humidity'],
                'wind_speed': weather_data['wind']['speed'],
            },
            'article': {
                'catastrophic': {
                    'headline': article_content.get('headline', None),
                    'lead': article_content.get('lead', None),
                    'body': article_content.get('body', None),
                },
                'sensational': {
                    'headline': article_content_2.get('headline', None),
                    'lead': article_content_2.get('lead', None),
                    'body': article_content_2.get('body', None),
                },
            }
        }
        return result, 200

    except requests.exceptions.HTTPError as http_err:
        error_message = f"HTTP error occurred: {http_err}"
        return {'error': error_message}, response.status_code

    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        return {'error': error_message}, 500

def generate_mock_weather_data(latitude, longitude):
        weather_conditions = [
            {'id': 200, 'main': 'Thunderstorm', 'description': 'thunderstorm with light rain', 'icon': '11d'},
            {'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'},
            {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'},
            {'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'},
            {'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'},
            {'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'},
        ]

        random_weather = random.choice(weather_conditions)
        random_temp = round(random.uniform(-10.0, 35.0), 2) 
        random_humidity = random.randint(20, 100)
        random_wind_speed = round(random.uniform(0.0, 15.0), 2)

        mock_weather_data = {
            'coord': {'lon': longitude, 'lat': latitude},
            'weather': [random_weather],
            'base': 'stations',
            'main': {
                'temp': random_temp,
                'feels_like': random_temp - random.uniform(0.5, 2.0),
                'temp_min': random_temp - random.uniform(0.0, 5.0),
                'temp_max': random_temp + random.uniform(0.0, 5.0),
                'pressure': random.randint(980, 1050),
                'humidity': random_humidity,
                'sea_level': random.randint(980, 1050),
                'grnd_level': random.randint(980, 1050)
            },
            'visibility': random.randint(5000, 10000),
            'wind': {
                'speed': random_wind_speed,
                'deg': random.randint(0, 360),
                'gust': random_wind_speed + random.uniform(0.0, 5.0)
            },
            'clouds': {'all': random.randint(0, 100)},
            'dt': int(datetime.utcnow().timestamp()),
            'sys': {
                'type': 1,
                'id': random.randint(1000, 10000),
                'country': 'XX',
                'sunrise': int(datetime.utcnow().replace(hour=6, minute=0, second=0).timestamp()),
                'sunset': int(datetime.utcnow().replace(hour=18, minute=0, second=0).timestamp())
            },
            'timezone': 0,
            'id': random.randint(100000, 999999),
            'name': 'Random City',
            'cod': 200
        }
        return mock_weather_data