import unittest
import sys
import clr
import imp
from System.IO import File
from os import path

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
  0.3 [2014.06.18]
"""

class TestItem(unittest.TestCase) :
  """
  class TestItem - Test XML item
  - Item count.
  - Extract property by name.
  - Extract collection by name.
  """
  def setUp(self) :
    parser = Parser()
    self.items = parser.extract()

  def testCollection(self) :
    collections = self.items[0].Collections
    d001 = collections["UW_D001"]
    length = len(d001)
    self.assertTrue(length > 0)

  def testField(self) :
    from Newtonsoft.Json import JsonConvert
    item = self.items[0]
    f1 = item.CLM_001D1
    f2 = item.UW_D001D10
    self.assertEqual(f2, "UW25570004074")

  def testItemCount(self) :
    length = len(self.items)
    self.assertEqual(length, 1)

class TestParser(unittest.TestCase) :
  """
  class TestParser - Test parser
  - Load xml file.
  - Load editor file.
  - Instantiate extractor.
  """
  def setUp(self):
    self.parser = Parser()

  def testMainSection(self) :
    editor = self.parser.getEditorObject()
    main = editor.Main
    self.assertFalse(main == None)
    self.assertTrue(main.startswith("import"))

  def testLoadXmlFile(self) :
    xml = self.parser.getXml()
    self.assertFalse(xml == "")

  def testLoadEditorFile(self) :
    # extract text from editor file.
    editorText = self.parser.getEditorText()
    self.assertFalse(editorText == None)
    self.assertFalse(editorText == "")

  def testLoadParser(self) :
    extractor = self.parser.getParser()
    self.assertFalse(extractor == None)

  def testInstantiate(self) :
    """
    Create extractor instance.
    Export object for another case.
    """
    Extractor = self.parser.getParser()
    inst = Extractor()
    self.assertFalse(inst == None)

class Parser() :

  def __init__(self) :
    """
    Load dependency files.
    """
    self.applicationPath = "E:/source/projects/oli.generator/Generator/bin/Debug"
    self.scriptPath = "E:/runtime/generator.env/Template.OLI_Template/Item.Script"

    self.editorFile = path.join(self.scriptPath, "93C9F52B82DA4A3F903B8E72E1B1DF77.SCRIPT.PY.EDITOR")
    self.parserFile = path.join(self.scriptPath, "93C9F52B82DA4A3F903B8E72E1B1DF77.SCRIPT.PY")
    self.sampleFile = path.join(self.scriptPath, "93C9F52B82DA4A3F903B8E72E1B1DF77.TEST.XML")

    self.appendPath()
    self.loadDLL()

  def appendPath(self) :
    """
    Append .net assemply path.
    """
    # append .dll|.exe path.
    sys.path.append(self.applicationPath)
    sys.path.append(self.scriptPath)

  def loadDLL(self) :
    """
    Load all dependency dll|exe.
    """
    # loadd dependency dll.
    clr.AddReference("Newtonsoft.Json.dll")
    clr.AddReference("Editor.exe")

  def getXml(self) :
    """
    Load xml from test file.
    """
    from System.IO import File
    xml = File.ReadAllText(self.sampleFile)
    return xml

  def getEditorText(self) :
    """
    Load parser text from file.
    File format: <\d{32}>.SCRIPT.PY.EDITOR
    Location: <Template Path>/Item.Script
    """
    editorText = File.ReadAllText(self.editorFile)
    return editorText

  def getParser(self) :
    """
    Load parser from file.
    File format: <\d{32}>.SCRIPT.PY
    Location: <Template Path>/Item.Script
    """
    script = imp.load_source('module.name', self.parserFile)
    return script.Extractor;

  def getEditorObject(self) :
    """
    Create object from editor text (json string).
    Use JsonConvert to deserialize json into PropertyEditor.
    """
    from Newtonsoft.Json import JsonConvert
    from Generator.Editor import PropertyEditor

    editorText = self.getEditorText()
    function = JsonConvert.DeserializeObject[PropertyEditor].Overloads[type("")]
    editorObject = function(editorText)
    return editorObject

  def extract(self) :
    """
    Extract xml into item.
    Each item contain properties and collections.
    """
    xml = self.getXml()
    editor = self.getEditorObject()
    parser = self.getParser()()
    parser.SetEditor(editor)
    result = parser.Extracts(xml)
    return result
