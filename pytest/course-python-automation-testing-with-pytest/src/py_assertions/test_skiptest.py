import pytest
import sys

pytestmark = pytest.mark.skipif(sys.platform == 'linux', reason="This only works on windows OS")

frac_value = 9/5

def cent_to_fah(temp=0):
    fah = (temp * frac_value) + 32
    return fah

#print(cent_to_fah())
@pytest.mark.skip(reason="Skipping this test, no need to prove it")
def test_case01():
    assert type(frac_value) == float

def test_case02():
    assert cent_to_fah() == 32

def test_case03():
    assert cent_to_fah(38) == 100.4

@pytest.mark.skipif(sys.version_info > (3,6), reason="Does not work with versions greater that 3.6")
def test_conditional_skip():
    assert False

@pytest.mark.skipif(sys.version_info < (3,6), reason="Does not work with older versions lower that 3.6")
def test_conditional_skip_older():
    assert True
