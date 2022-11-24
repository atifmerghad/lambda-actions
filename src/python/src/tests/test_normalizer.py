import unittest


class MyTestCase(unittest.TestCase):
    def test_good_items(self):
        # Check Kpi
        self.assertEqual("ABC", "ABC")
    def test_bad_items(self):
        # Check Kpi
        self.assertEqual("ABC", "CDF")
        
    
        

if __name__ == '__main__':
    unittest.main()
