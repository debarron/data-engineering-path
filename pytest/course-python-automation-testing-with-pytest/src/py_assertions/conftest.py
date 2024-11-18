import pytest

def pytest_configure():
    pytest.weekdays1 = ['mon', 'tue', 'wed']
    pytest.weekdays2 = ['fri', 'sat', 'sun']


@pytest.fixture(scope="module")
def global_inp_list():
    return [1,2,3,4,5]


@pytest.fixture(scope="module")
def global_setup_weekdays1():
    w1 = pytest.weekdays1.copy()
    w1.append('thur')
    yield w1

    # Run teardown to set w1 back to normal
    w1.pop()

@pytest.fixture()
def global_setup_weekdays2():
    w2 = pytest.weekdays2.copy()
    w2.insert(0, 'thur')
    yield w2


