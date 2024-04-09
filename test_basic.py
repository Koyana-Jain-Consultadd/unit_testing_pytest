

from basic import *
# import pytest

# @pytest.mark.number
def test_add():
    assert add(1,2)==3
    assert add(5)==7

# @pytest.mark.number
def test_prod():
    assert product(2,7)==14
    assert product(7,7)==49

# @pytest.mark.strings
def test_add_str():
    res=add('Hello',' World')
    assert res=='Hello World'
    assert type(res) is str
    assert 'Hello' in res

# @pytest.mark.strings
def test_prod_str():
    assert product('Hello ',3)=='Hello Hello Hello ' 
    res=product('Hello ',2)
    assert res=='Hello Hello '
    assert type(res) is str
    assert 'Hello' in res