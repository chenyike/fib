#author - Yike Chen

import unittest
from fib import *

class Test_fib(unittest.TestCase):
    
    def test_Fn(self):
        self.assertEqual(F(0),0)
        self.assertEqual(F(1),1)
        self.assertEqual(F(2),1)
        self.assertEqual(F(3),2)
        self.assertEqual(F(4),3)
        
    def test_is_prime_number(self):
        self.assertEqual(is_prime_number(0),False)
        self.assertEqual(is_prime_number(1),False)
        self.assertEqual(is_prime_number(2),True)
        self.assertEqual(is_prime_number(3),True)
        self.assertEqual(is_prime_number(4),False)
        self.assertEqual(is_prime_number(5),True)
        self.assertEqual(is_prime_number(6),False)

    def test_outPut(self):
        self.assertEqual(outPut(1),1)
        self.assertEqual(outPut(0),"Buzz")
        self.assertEqual(outPut(3),"FizzBuzz")
        self.assertEqual(outPut(5),"Fizz")
        self.assertEqual(outPut(9),34)

unittest.main()
