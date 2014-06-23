import unittest

class Test(unittest.TestCase) :
    def testImport(self) :
        mod = __import__("experiment.lib", fromlist= ["Library"])
        Library = getattr(mod, "Library")
        lib = Library()
        lib.show()
        self.assertFalse(lib == None)
