import clr
from test.wrapper import timed
from os import path
import sys
import imp
import System.IO
from System.IO import File

class Parser() :
    """
    class Parser - Parser xml file and extract item. """

    def __init__(self) :
        """ Load dependency files. """

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
        """ Append .net assemply path. """

        # append .dll|.exe path.
        sys.path.append(self.applicationPath)
        sys.path.append(self.scriptPath)


    @timed
    def loadDLL(self) :
        """ Load all dependency dll|exe. """

        # loadd dependency dll.
        clr.AddReference("Newtonsoft.Json.dll")
        clr.AddReference("Editor.exe")

    @timed
    def getXml(self) :
        """ Load xml from test file. """

        from System.IO import File
        xml = File.ReadAllText(self.sampleFile)
        return xml

    @timed
    def getEditorText(self) :
        """ Load parser text from file.
        File format: <\d{32}>.SCRIPT.PY.EDITOR
        Location: <Template Path>/Item.Script """

        editorText = File.ReadAllText(self.editorFile)
        return editorText

    @timed
    def getParser(self) :
        """ Load parser from file.
        File format: <\d{32}>.SCRIPT.PY
        Location: <Template Path>/Item.Script """

        script = imp.load_source('module.name', self.parserFile)
        return script.Extractor;

    @timed
    def getEditorObject(self) :
        """ Create object from editor text (json string).
        Use JsonConvert to deserialize json into PropertyEditor. """

        from Newtonsoft.Json import JsonConvert
        from Generator.Editor import PropertyEditor

        editorText = self.getEditorText()
        function = JsonConvert.DeserializeObject[PropertyEditor].Overloads[type("")]
        editorObject = function(editorText)
        return editorObject

    @timed
    def extract(self) :
        """ Extract xml into item.
        Each item contain properties and collections. """

        xml = self.getXml()
        parser = self.getParser()()
        result = parser.Extracts(xml)
        return result
