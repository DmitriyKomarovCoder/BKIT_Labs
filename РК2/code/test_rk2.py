import unittest
import rk1

class Test_field(unittest.TestCase):
    def setUp(self):
        self.test1 = [('Intel Core i5-12500k', 4, 'MacBook'), ('Intel Core i9-9000', 16, 'ThinkPad')]
        self.test2 = [('MacBook', 4), ('MateBookX', 4), ('ThinkPad', 16), ('ThinkPad', 16)]
        self.test3 = [('AMD Ryzen 5', 4, 'Inspiron'), ('AMD Ryzen 3', 32, 'Inspiron'), ('AMD Ryzen 8', 12, 'Inspiron'), ('Intel Core i5-12500k', 4, 'Latitude'), ('Intel Core i5-12500k', 4, 'MacBook'), ('AMD Ryzen 5', 4, 'MateBookX'), ('AMD Ryzen 3', 32, 'MateBookX'), ('AMD Ryzen 8', 12, 'MateBookX'), ('Intel Core i9-9000', 16, 'ThinkPad'), ('Intel Core i9-9000', 16, 'ThinkPad')]
    
    def test1_rk(self):
        self.assertEqual(rk1.task1(rk1.computers, rk1.microprocessor), self.test1)

    def test2_rk(self):
        self.assertEqual(rk1.task2(rk1.computers, rk1.microprocessor), self.test2)

    def test3_rk(self):
        self.assertEqual(rk1.task3(rk1.computers, rk1.microp_comp, rk1.microprocessor), self.test3)

if __name__ == '__main__':
    unittest.main()