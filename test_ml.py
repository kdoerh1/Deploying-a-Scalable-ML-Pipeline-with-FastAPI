import pytest

def test_1():
    """
    This test is to make sure 5 times 5 = 25
    """
    assert 5*5==25
    

def test_2():
    """
    This test is to make sure the .upper() function works
    """
    assert "yummy".upper()=='YUMMY'
    


def test_3():
    """
    This test is to make sure the length function works
    """
    assert len("yummy") ==5
    
