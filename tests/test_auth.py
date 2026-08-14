import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from auth import get_current_user


def test_user_1_token():
    credentials = HTTPAuthorizationCredentials(
        scheme="Bearer",
        credentials="user_1"
    )

    assert get_current_user(credentials) == "user_1"


def test_user_2_token():
    credentials = HTTPAuthorizationCredentials(
        scheme="Bearer",
        credentials="user_2"
    )

    assert get_current_user(credentials) == "user_2"


def test_invalid_token():
    credentials = HTTPAuthorizationCredentials(
        scheme="Bearer",
        credentials="invalid_user"
    )

    with pytest.raises(HTTPException) as error:
        get_current_user(credentials)

    assert error.value.status_code == 401