import unittest

from match import weekday_message


class TestWeekdayMessage(unittest.TestCase):
    def test_monday(self):
        self.assertEqual(weekday_message(1), "Today is Monday")

    def test_tuesday(self):
        self.assertEqual(weekday_message(2), "Today is Tuesday")

    def test_wednesday(self):
        self.assertEqual(weekday_message(3), "Today is Wednesday")

    def test_thursday(self):
        self.assertEqual(weekday_message(4), "Today is Thursday")

    def test_friday(self):
        self.assertEqual(weekday_message(5), "Today is Friday")

    def test_saturday(self):
        self.assertEqual(weekday_message(6), "Today is Saturday")

    def test_sunday(self):
        self.assertEqual(weekday_message(7), "Today is Sunday")

    def test_invalid_day(self):
        self.assertEqual(weekday_message(0), "Invalid day")
        self.assertEqual(weekday_message(8), "Invalid day")


if __name__ == "__main__":
    unittest.main()
