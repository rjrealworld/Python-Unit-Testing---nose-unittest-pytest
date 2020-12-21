import unittest
from odometer import Odometer

class TestOdometer(unittest.TestCase):
    
    def setUp(self):
        self.o2 = Odometer(2)

    def test_ascending(self):
        self.assertEqual(Odometer.is_ascending(11), False)
        self.assertEqual(Odometer.is_ascending(-123), True)
        self.assertEqual(Odometer.is_ascending(2), True)
        self.assertEqual(Odometer.is_ascending(123456789), True)
        self.assertEqual(Odometer.is_ascending(12.34), True)
    
    def test_next_reading(self):
        #getting back the starting pos after adding length
        length = self.o2.LENGTH
        self.o2.next_reading(length)
        self.assertEqual(self.o2.readings[self.o2.position], 12) 
        
        #adding 1 to the above obtained reading
        self.o2.next_reading(1)
        self.assertEqual(self.o2.readings[self.o2.position], 13) 
        
        #adding 7 to the above reading
        self.o2.next_reading(7)
        self.assertEqual(self.o2.readings[self.o2.position], 23)
        
    
    def test_prev_reading(self):
        length = self.o2.LENGTH
        self.o2.prev_reading(length)
        self.assertEqual(self.o2.readings[self.o2.position], 12) 
        
        self.o2.prev_reading(1)
        self.assertEqual(self.o2.readings[self.o2.position], 89) 
        
        self.o2.prev_reading(10)
        self.assertEqual(self.o2.readings[self.o2.position], 49)
        
    
    def test_diff(self, o = 1):
        pass

if __name__ == '__main__':
    unittest.main()
