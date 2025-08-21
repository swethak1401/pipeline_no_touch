import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home_route():
    """Tests the home route for a 200 OK response."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.json['message'] is not None

def test_health_check_route():
    """Tests the health check route."""
    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        assert response.json['status'] == 'ok'