from basic import *
import pytest

@pytest.mark.parametrize('x,y,res',
                         [
                             (7,3,10),
                             (2,4,6),
                             ('Hello',' World','Hello World'),
                             (10.5,25.5,36)
                         ])
def test_add(x,y,res):
    assert add(x,y)==res
    