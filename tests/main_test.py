import pytest

from app import create_app, db
from app.models import Feature

from datetime import datetime


@pytest.fixture
def web():
    app = create_app('testing')
    ctx = app.app_context()
    ctx.push()

    db.create_all()

    yield app.test_client()

    db.drop_all()
    db.session.remove()

    ctx.pop()

def test_feature_api(web):
    new_feature = Feature(
        title= 'Feature 1',
        description= 'Feature 1',
        client='Client A',
        client_priority=1,
        target_date= datetime(2020, 3, 3, 10, 10, 10),
        product_area='Policies',
    )
    db.session.add(new_feature)
    db.session.commit()

    response = web.get("/")
    assert response.status == '200 OK'

    response = web.get("/update/1/")
    assert response.status == '200 OK'

    response = web.get("/delete/1/")
    assert response.status == '200 OK'
