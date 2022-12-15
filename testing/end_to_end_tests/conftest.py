import pytest

def pytest_addoption(parser):
    parser.addoption("--apikey", action="store")

@pytest.fixture(scope='session')
def api_key(request):
    api_key = request.config.option.apikey
    assert api_key is not None
    return api_key