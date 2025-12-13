from app import app


def test_home_route():
    assert callable(app)
