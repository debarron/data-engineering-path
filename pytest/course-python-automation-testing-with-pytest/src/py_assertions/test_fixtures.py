import pytest
import os

@pytest.fixture()
def _inp_list():
    return [1,2,3,4,5]

def test_fixture(_inp_list):
    assert [1,2,3] == _inp_list[:3]

@pytest.mark.xfail
@pytest.mark.usefixtures("_inp_list")
def test_run_fixture():
    assert _inp_list[0] == 1


weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']

@pytest.fixture()
def setup_weekdays1():
    w1 = weekdays1.copy()
    w1.append('thur')
    yield w1

    # Run teardown to set w1 back to normal
    w1.pop()

@pytest.fixture()
def setup_weekdays2():
    w2 = weekdays2.copy()
    w2.insert(0, 'thur')
    yield w2

def test_list_teardown(setup_weekdays1):
    setup_weekdays1.extend(weekdays2)
    assert setup_weekdays1 == ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']

def test_multiple_fixtures(setup_weekdays1, setup_weekdays2):
    assert len(setup_weekdays2) == len(setup_weekdays1)

filename = "file1.txt"
@pytest.fixture()
def setup_file():
    f = open(filename, "w")
    f.write("Python is good")
    f.close()

    f = open(filename, "r")
    yield f

    f.close()
    os.remove(filename)

def test_file_fixture(setup_file):
    assert setup_file.readline() == "Python is good"


def test_global_fixtures(_inp_list, global_inp_list):
    assert len(_inp_list) == len(global_inp_list)
