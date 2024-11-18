import pytest

def test_exception():
    with pytest.raises(Exception):
        assert (1/0)


def test_specific_exception():
    with pytest.raises(ZeroDivisionError):
        assert (1/0)


def test_miss_exception():
    with pytest.raises(ZeroDivisionError):
        a = [1,1]
        #assert a[1] == 1
        assert a[1]/0


def throws_exception():
    raise ValueError("Some value error")

def test_check_exception_type():
    with pytest.raises(ValueError) as err:
        throws_exception()

    print(err.value)
    assert err.value != ""
