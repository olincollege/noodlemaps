import pytest
import src.app as webapp


@pytest.fixture()
def app():
    """
    Creates, sets up, and tears down the app for this testing session

    :return: the Flask app to test on
    """
    app = webapp.app
    app.config.update({'TESTING': True})
    yield app


@pytest.fixture()
def client(app):
    """
    :return: The testing client for this test session
    """
    return app.test_client()


def test_form_get(client):
    """
    Tests the GET method in /form

    :param client: the Flask test client to test on
    """
    response = str(client.get('/form').data)
    assert '<form' in response
    assert '<input type="submit"' in response


def test_form_post(client, api_key):
    """
    Tests the POST method in /form

    :param client: the Flask test client to test on
    """
    start = 'Boston, MA'
    end = '1000 Olin Way, Needham MA'
    midpoints = ['Cambridge MA', 'Concord MA', 'Framingham MA', 'Wellesley MA']
    data = {
        'start': start,
        'end': end,
        'midpoints': ','.join(midpoints),
        'key': api_key,
    }
    response = client.post('/form', data=data)
    assert response.status_code == 200
