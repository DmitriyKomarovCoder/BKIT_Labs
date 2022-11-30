import unittest
from lab_python_fp.field import field
from lab_python_fp.sort import sort_abs

class Test_field(unittest.TestCase):
    def setUp(self):
        self.goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
        ]
        self.data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    def test_field1(self):
        self.assertEqual(list(field(self.goods, 'title')), ['Ковер', 'Диван для отдыха'])

    def test_fied2(self):
        self.assertEqual(list(field(self.goods, 'title', 'price')), [{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}])

    def test_sort(self):
        self.assertEqual(sort_abs(self.data), [123, 100, -100, -30, 4, -4, 1, -1, 0])

if __name__ == '__main__':
    unittest.main()