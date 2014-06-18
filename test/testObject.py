from unittest import TestCase

class Expendo(object):
    pass

class  TestObject(TestCase) :
    def testExpendo(self) :
        ex = Expendo()
        ex.a001 = "100"
        ex.a002 = "200"
        ex.a003 = "300"

        atts = [x for x in ex.__dict__]
        print(atts)
        self.assertEqual(len(atts), 3)

        values = [x for x in ex.__dict__.values()]
        print(values)
        self.assertEqual(len(values), 3)
