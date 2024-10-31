
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_generate_article_success(client, mocker):
    # Mockovanie volania OpenAI API a weather_service
    mocker.patch('weather_app.services.weather_service.get_current_weather', return_value=({'temperature': 20, 'description': 'clear sky', 'location': 'Bratislava'}, 200))
    mocker.patch('openai.Completion.create', return_value=MockResponse())

    data = {
        'location': 'Bratislava',
        'language': 'en',
        'style': 'factual'
    }
    response = client.post('/article/generate', json=data)
    assert response.status_code == 201
    data = response.get_json()
    assert 'article_id' in data

def test_generate_article_missing_fields(client):
    data = {'location': 'Bratislava'}
    response = client.post('/article/generate', json=data)
    assert response.status_code == 400
    data = response.get_json()
    assert 'errors' in data
