
import sys
sys.path.append('.')
print sys.path
from a.a import test_a1
from b2 import test_b2

def test_b1():
    test_a1()
    print "b1"
    test_b2()



test_b1()
