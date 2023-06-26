import unittest
import datetime
from date_func import date 
formated_date, formated_time, formated_weekday = date()
class DateFuncTestCase(unittest.TestCase):
    
    def test_date_format(self):
        today = datetime.datetime.today().date()
        expected_date = today.strftime("%d %B, %Y")
        actual_date = formated_date
        self.assertEqual(actual_date, expected_date)

    def test_time_format(self):
        today = datetime.datetime.today().date()
        expected_time = today.strftime("%I:%M %p")
        actual_time = formated_time
        self.assertEqual(actual_time, expected_time)

    def test_weekday_format(self):
        today = datetime.datetime.today().date()
        expected_weekday = today.strftime("%a")
        actual_weekday = formated_weekday
        self.assertEqual(actual_weekday, expected_weekday)

    def test_output_consistency(self):
        output1 = date
        output2 = date
        self.assertEqual(output1, output2)

if __name__ == '__main__':
    unittest.main()
