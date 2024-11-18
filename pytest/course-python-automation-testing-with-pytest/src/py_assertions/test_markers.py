import pytest
pytestmark = [pytest.mark.critical, pytest.mark.smoke]

def test_val01():
    assert True

@pytest.mark.str_test
def test_val02():
    assert len("Hello") > 0

@pytest.mark.str_test
@pytest.mark.critical
def test_val03():
    assert "Hi" in "Hi my name is WHAT?"

@pytest.mark.critical
def test_val05():
    assert 1 != 0
