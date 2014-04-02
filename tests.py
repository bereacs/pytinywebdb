import unittest
from tinywebdb import TinyWebDB

# https://docs.python.org/2/library/unittest.html

# Run with
# python tests.py

class TinyWebDBTests(unittest.TestCase):

    def setUp(self):
      pass

    # Test the proper attachment of a trailing slash for one parameter.
    def test_constructor1 (self):
      self.tdb1 = TinyWebDB("berea.edu", "tinywebdb")
      self.assertEqual(self.tdb1.getURL(), "http://berea.edu/tinywebdb/")
      self.tdb1 = TinyWebDB("berea.edu", "tinywebdb/")
      self.assertEqual(self.tdb1.getURL(), "http://berea.edu/tinywebdb/")
    
    # Test the proper attachment of middle/trailing slash for two parameters.
    def test_constructor2 (self):
      self.tdb2 = TinyWebDB("http://berea.edu/tinywebdb", "matt")
      self.assertEqual(self.tdb2.getURL(), "http://berea.edu/tinywebdb/matt/")
      self.tdb2 = TinyWebDB("http://berea.edu/tinywebdb/", "matt")
      self.assertEqual(self.tdb2.getURL(), "http://berea.edu/tinywebdb/matt/")
      self.tdb2 = TinyWebDB("http://berea.edu/tinywebdb", "matt/")
      self.assertEqual(self.tdb2.getURL(), "http://berea.edu/tinywebdb/matt/")
      self.tdb2 = TinyWebDB("http://berea.edu/tinywebdb/", "matt/")
      self.assertEqual(self.tdb2.getURL(), "http://berea.edu/tinywebdb/matt/")
      
if __name__ == '__main__':
    unittest.main()