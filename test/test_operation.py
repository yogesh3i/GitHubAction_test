from src.math_op import addi,subs

def test_add():
    assert addi(2,3)==5
    assert addi(9,9)==18 

def test_sub():
    assert subs(5,2)==3
    assert subs(5,4)==1 