"""
Run:
    1. Open command prompt.
    2. ipy -m unittest testParser.<ClassName>

Example:
    ipy -m unittest testParser.TestItem
    ipy -m unittest testParser.TestParser

Revision:
    0.1 [2014.06.16] Add Parser, TestParser and TestItem.
    0.2 [2014.06.17]
    0.3 [2014.06.18]   """


import unittest
import imp
from System.IO import File
from test.wrapper import timed
from test.parser import Parser

class TestItem(unittest.TestCase) :
    """
    class TestItem - Test XML item
    - Item count.
    - Extract property by name.
    - Extract collection by name. """

    @timed
    def setUp(self) :
        parser = Parser()
        self.items = parser.extract()

        #from Newtonsoft.Json import JsonConvert
        #json = JsonConvert.SerializeObject(self.items)

    @timed
    def testCollection(self) :
        """
        Test collection. """

        collections = self.items[0].Collections
        d001 = collections["C001"]
        length = len(d001)
        self.assertTrue(length > 0)

    @timed
    def testField(self) :
        """
        Check specific field value. """

        from Newtonsoft.Json import JsonConvert
        item = self.items[0]
        atts = [x for x in item.__dict__]
        self.assertFalse(len(atts) == 0)

    @timed
    def testItemCount(self) :
        """
        Check number of items in xml. """
        length = len(self.items)
        self.assertEqual(length, 211)
