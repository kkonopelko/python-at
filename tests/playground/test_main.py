from playground.main import A

def test_main():
    assert A.x == 1

def test_sum():
    x = 1
    y = 2
    assert x + y == 3