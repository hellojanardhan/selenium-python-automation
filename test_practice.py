import pytest
@pytest.mark.parametrize("a,b", [(1, 2), (3, 5), (5, 6)])
def test_add(a, b):
    result = a + b
    if result <= 10:
        pytest.fail(f"Sum is too small: {result}")