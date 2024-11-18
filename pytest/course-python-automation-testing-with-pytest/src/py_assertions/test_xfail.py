import pytest

@pytest.mark.xfail
def test_to_fail():
    assert False

@pytest.mark.xfail(True == True, reason="This fails to learn")
def test_will_fail():
    assert True

@pytest.mark.xfail(raises=ValueError, reason="we need to learn")
def test_failed_value():
    raise ValueError("blah!")


@pytest.mark.xfail(raises=TypeError, reason="we need to learn")
def test_failed_type():
    raise valueerror("blah!")


