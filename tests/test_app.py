from app import index,add
import pytest

def test():
	assert index()=="Hello world"

@pytest.mark.parametrize('x,y,result',[
	(10,10,20),(5,3,8),(9,0,9)
])
def test_add(x,y,result):
	assert add(x,y)==result