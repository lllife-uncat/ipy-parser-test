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
import sys
import clr
import imp
from System.IO import File
from os import path
from wrapper import timed

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

class TestParser(unittest.TestCase) :
    """
    class TestParser - Test parser
    - Load xml file.
    - Load editor file.
    - Instantiate extractor. """

    def setUp(self):
        """
        Init parser. """
        self.parser = Parser()

    def testGrun(self):
        self.assertEqual(0,0)

    def testMainSection(self) :
        """
        Extract main section from editor. """

        editor = self.parser.getEditorObject()
        main = editor.Main
        self.assertFalse(main == None)
        self.assertTrue(main.startswith("import"))

    def testLoadXmlFile(self) :
        """
        Load xml file from script path. """

        xml = self.parser.getXml()
        self.assertFalse(xml == "")

    def testLoadEditorFile(self) :
        """
        Load editor file from script path. """

        # extract text from editor file.
        editorText = self.parser.getEditorText()
        self.assertFalse(editorText == None)
        self.assertFalse(editorText == "")

    def testLoadParser(self) :
        """
        Load parser (.py) from script path. """

        extractor = self.parser.getParser()
        self.assertFalse(extractor == None)

    def testInstantiate(self) :
        """
        Create extractor instance.
        Export object for another case. """

        Extractor = self.parser.getParser()
        inst = Extractor()
        self.assertFalse(inst == None)

class Parser() :
    """
    class Parser - Parser xml file and extract item. """

    def __init__(self) :
        """
        Load dependency files. """

        from configs import Setting
        s = Setting()

        self.applicationPath =  s.applicationPath
        self.scriptPath = s.scriptPath
        self.sampleFile = s.sampleFile

        self.editorFile = path.join(self.scriptPath, s.uuid + ".SCRIPT.PY.EDITOR")
        self.parserFile = path.join(self.scriptPath, s.uuid + ".SCRIPT.PY")

        self.appendPath()
        self.loadDLL()

    @timed
    def appendPath(self) :
        """
        Append .net assemply path. """

        # append .dll|.exe path.
        sys.path.append(self.applicationPath)
        sys.path.append(self.scriptPath)


    @timed
    def loadDLL(self) :
        """
        Load all dependency dll|exe. """

        # loadd dependency dll.
        clr.AddReference("Newtonsoft.Json.dll")
        clr.AddReference("Editor.exe")

    @timed
    def getXml(self) :
        """
        Load xml from test file. """

        from System.IO import File
        xml = File.ReadAllText(self.sampleFile)
        return xml

    @timed
    def getEditorText(self) :
        """
        Load parser text from file.
        File format: <\d{32}>.SCRIPT.PY.EDITOR
        Location: <Template Path>/Item.Script """

        editorText = File.ReadAllText(self.editorFile)
        return editorText

    @timed
    def getParser(self) :
        """
        Load parser from file.
        File format: <\d{32}>.SCRIPT.PY
        Location: <Template Path>/Item.Script """

        script = imp.load_source('module.name', self.parserFile)
        return script.Extractor;

    @timed
    def getEditorObject(self) :
        """
        Create object from editor text (json string).
        Use JsonConvert to deserialize json into PropertyEditor. """

        from Newtonsoft.Json import JsonConvert
        from Generator.Editor import PropertyEditor

        editorText = self.getEditorText()
        function = JsonConvert.DeserializeObject[PropertyEditor].Overloads[type("")]
        editorObject = function(editorText)
        return editorObject

    @timed
    def extract(self) :
        """
        Extract xml into item.
        Each item contain properties and collections. """

        xml = self.getXml()
        parser = self.getParser()()
        result = parser.Extracts(xml)
        return result
