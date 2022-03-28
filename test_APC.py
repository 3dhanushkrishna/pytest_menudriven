import APC
import pytest
@pytest.mark.squarerectangle

def test_square():
    a=2
    res=APC.square(a)
    assert res==a**2
@pytest.mark.squarerectangle
def test_perimeter():
    a=3
    b=4
    res=APC.perimeter(a,b)
    assert  res==2*(a+b)
@pytest.mark.squarerectangle
def test_rectangle():
    a=4
    b=5
    res=APC.rectangle(a,b)
    assert res== a*b