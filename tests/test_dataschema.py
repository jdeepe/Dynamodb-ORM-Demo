import pytest
from moto import mock_dynamodb2

from api.app import create_app
from settings import Config

from . import load_data, verify_settings


@mock_dynamodb2
def test_dataschema(client):
    load_data()
    data = {
        "name": "WorkOrder_v1",
    }
    response = client.get("/v1/dataschema/", json=data)
    assert response.status_code == 200

    data = {
        "name": "WorkOrder_v1",
        "dataset": "WorkOrder_v1",
        "status": "RETIRED",
        "description": "Schema for WO1",
        "last_updated_timestamp": "2017-12-24T22:38:47.346Z",
        "version": 2,
    }
    response = client.post("/v1/dataschema/", json=data)
    assert response.status_code == 200
    verify_settings("DataSchema", data["name"], data)


@mock_dynamodb2
def test_dataschema_list(client):
    load_data()
    response = client.post("/v1/dataschema/list", json={})
    data = {"nextToken": response.json["data"]["listDataSchemas"]["nextToken"]}
    response = client.post("/v1/dataschema/list", json=data)
    assert response.status_code == 200


@pytest.fixture
def client():
    app = create_app(Config)
    client = app.test_client()
    return client
