import random

import pytest
from core import create_app, db
from core.models import Movie

api = '/api/produtoras/intervalo_premiacoes'


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            db.session.commit()
            yield client
            db.drop_all()


def test_intervalo_premiacoes(client):
    response = client.get(api)
    assert response.status_code == 200
    data = response.get_json()
    assert "max" in data
    assert "min" in data
    assert isinstance(data["max"], list)
    assert isinstance(data["min"], list)


def test_load_award_intervals(client):
    response = client.get(api)
    assert response.status_code == 200
    data = response.get_json()

    assert len(data["max"]) > 0, "Deve haver pelo menos um intervalo máximo"
    assert len(data["min"]) > 0, "Deve haver pelo menos um intervalo mínimo"
    for entry in data["max"] + data["min"]:
        assert entry["interval"] >= 0, "Intervalo não pode ser negativo"
        assert entry["followingWin"] > entry["previousWin"], "followingWin deve ser maior que previousWin"
