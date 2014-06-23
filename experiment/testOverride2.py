"""
[Run]
python -m unittest testOverride
"""
import unittest

class A(object) :
  def __init__(self) :
    pass

  def getValue(self) :
    return "A value"

class B(A) :
  def __init__(self) :
    super(A, self).__init__()

  def getValue(self) :
    return "B value"

class Test(unittest.TestCase) :
  def testOverride(self) :
    b = B()
    value = b.getValue()
    self.assertEqual(value, "B value")
