# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:00:20 2018

@author: eugenr
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:06:16 2018

@author: eugenr
"""

import unittest
from user_interface import main_test

class MyTest(unittest.TestCase):
   def test_my_function(self):
        self.assertEqual(main_test(0), -1)
        self.assertEqual(main_test(1), 1)
        self.assertEqual(main_test(2), 2)
        self.assertEqual(main_test(3), 3)
        self.assertEqual(main_test(4), 4)
        self.assertEqual(main_test(5), 5)
        self.assertEqual(main_test(6), 6)
        self.assertEqual(main_test(7), 7)
        self.assertEqual(main_test(8), 8)
        self.assertEqual(main_test(9), 9)
        self.assertEqual(main_test(10), 10)
        self.assertEqual(main_test(15), -1)
        self.assertEqual(main_test(-5), -1)
        
if __name__ == '__main__':
    unittest.main()
    
