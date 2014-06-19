import unittest
import sys
import clr

class TestPah(unittest.TestCase) :
  def setUp(self) :
    sys.path.append("E:/source/projects/oli.generator/Generator/bin/Debug")
    clr.AddReference("Editor.exe")

if __name__ == "__main__" :
  unittest.main()
