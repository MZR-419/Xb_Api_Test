import pytest
import common.get_headers

@pytest.fixture(scope = "session")
def get_token():
    token = common.get_headers.get_token()
    return token
