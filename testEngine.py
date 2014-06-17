from testParser import TestParser
from configs import Setting
from wrapper import timed

import unittest
import sys
import clr
import System

clr.AddReference("System.Xml")
clr.AddReference("System.Xml.Linq")
clr.AddReference("System.Core")

clr.ImportExtensions(System.Linq)
clr.ImportExtensions(System.Xml.XPath)

class TestEngine(unittest.TestCase) :

    def setUp(self) :
        setting = Setting()
        self.scriptPath = setting.scriptPath
        self.applicationPath = setting.applicationPath
        self.sampleFile = r"E:\source\projects\oli.generator\Xml.Test\OBDElixir_1.xml"

        sys.path.append(self.applicationPath)
        clr.AddReference("Editor.exe")

    @timed
    def getItems(self) :
        from Generator.Models.Template import XParser
        from System.IO import File

        xml = File.ReadAllText(self.sampleFile)
        elements = XParser.XMLToXElements(xml, "item")

        items = []
        for element in elements :
            items.append(element)
        return items

    @timed
    def testItemLength(self) :
        items = self.getItems()
        self.assertEqual(items.Count , 211)

    @timed
    def testSerialize(self) :
        item = self.getItems()[0]
        eid = item.XPathEvaluate("/elixirid")

        self.assertFalse(eid == None)

    @timed
    def testPath(self) :
        self.assertFalse(self.scriptPath == None)
        self.assertFalse(self.applicationPath == None)

    @timed
    def testSaxParser(self) :
        items = self.getItems()
        self.assertTrue(len(items) > 0)
