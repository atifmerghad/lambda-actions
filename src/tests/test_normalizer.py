import unittest


class MyTestCase(unittest.TestCase):
    def test_good_items(self):
        # Check Kpi
        self.assertEqual("ABC", "ABC")
        
    
        

if __name__ == '__main__':
    unittest.main()
