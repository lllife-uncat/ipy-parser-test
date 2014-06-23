import unittest
import System.IO
from test.parser import Parser

class TestParser(unittest.TestCase) :
    """
    class TestParser - Test parser
    - Load xml file.
    - Load editor file.
    - Instantiate extractor. """

    def setUp(self):
        """ Init parser. """
        self.parser = Parser()

    def testGrun(self):
        self.assertEqual(0,0)

    def testMainSection(self) :
        """ Extract main section from editor. """

        editor = self.parser.getEditorObject()
        main = editor.Main
        self.assertFalse(main == None)
        self.assertTrue(main.startswith("import"))

    def testLoadXmlFile(self) :
        """ Load xml file from script path. """

        xml = self.parser.getXml()
        self.assertFalse(xml == "")

    def testLoadEditorFile(self) :
        """ Load editor file from script path. """

        # extract text from editor file.
        editorText = self.parser.getEditorText()
        self.assertFalse(editorText == None)
        self.assertFalse(editorText == "")

    def testLoadParser(self) :
        """ Load parser (.py) from script path. """

        extractor = self.parser.getParser()
        self.assertFalse(extractor == None)

    def testInstantiate(self) :
        """ Create extractor instance.
        Export object for another case. """

        Extractor = self.parser.getParser()
        inst = Extractor()
        self.assertFalse(inst == None)
