# tests/test_weather.py
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_current_weather(client):
    response = client.get('/weather/current?location=Bratislava')
    assert response.status_code == 200
    data = response.get_json()
    assert 'temperature' in data
def test_current_weather_missing_location(client):
    response = client.get('/weather/current')
    assert response.status_code == 400
    data = response.get_json()
    assert 'errors' in data

def test_current_weather_invalid_language(client):
    response = client.get('/weather/current?location=Bratislava&language=de')
    assert response.status_code == 400
    data = response.get_json()
    assert 'errors' in data
