import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Teste simples para ver se a rota '/' responde com código 200 (OK)"""
    response = client.get('/')
    assert response.status_code == 200