# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:00:20 2018

@author: eugenr
"""
import unittest
from test_func import test_func

class MyTest(unittest.TestCase):
   def test_my_function(self):
        self.assertEqual(test_func(0), -1)
        self.assertEqual(test_func(1), 1)
        self.assertEqual(test_func(2), 2)
        self.assertEqual(test_func(3), 3)
        self.assertEqual(test_func(4), 4)
        self.assertEqual(test_func(5), 5)
        self.assertEqual(test_func(6), 6)
        self.assertEqual(test_func(7), 7)
        self.assertEqual(test_func(8), 8)
        self.assertEqual(test_func(9), 9)
        self.assertEqual(test_func(10), 10)
        self.assertEqual(test_func(15), -1)
        self.assertEqual(test_func(-5), -1)
        
if __name__ == '__main__':
    unittest.main()
    
