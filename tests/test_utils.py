import pytest

from src.utils import divide, get_user


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_get_user_found():
    users = [{"id": 1, "name": "Ana"}, {"id": 2, "name": "Luis"}]
    assert get_user(users, 2) == {"id": 2, "name": "Luis"}


def test_get_user_not_found_returns_none():
    users = [{"id": 1, "name": "Ana"}]
    assert get_user(users, 99) is None
