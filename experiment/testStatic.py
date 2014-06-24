
import unittest

class Test(object) :
    def __init__(self):
        pass

    @staticmethod
    def run() :
        print "Hello"
        return True



class TestStatic(unittest.TestCase) :

    def testStatic(self) :
        rs = Test.run()
        self.assertEqual(rs, True)
