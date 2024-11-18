import pytest
from math import prod

@pytest.mark.parametrize('arg', [1,2,3])
def test_val(arg):
    assert arg > 0

@pytest.mark.parametrize("inp, out", [(2,4), (3,27), (4,256)])
def test_param(inp, out):
    assert (inp ** inp) == out


data = [
    ([2,3,4], 'sum', 9),
    ([2,3,4], 'prod', 24),
]
@pytest.mark.parametrize("inp, operation, result", data)
def test_math_funcs(inp, operation, result):
    if operation == "sum":
        assert sum(inp) == result
    elif operation == "prod":
        assert prod(inp) == result
