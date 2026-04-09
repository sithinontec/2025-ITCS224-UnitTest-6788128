import unittest
from age import categorize_by_age

class TestIschild(unittest.TestCase):
    def test_child_age(self):
        for age in range(0, 10):  # 0 to 9
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Child")
                print(f"{age} is considered as a child.")

class TestIsadult(unittest.TestCase):
    def test_adult_age(self):
        for age in range(19, 66):  # 19 to 65
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adult")
                print(f"{age} is considered as an adult.")

class TestIsgolden(unittest.TestCase):
    def test_golden_age(self):
        for age in range(66, 151):  # 66 to 150
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Golden age")
                print(f"{age} is considered as golden age.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
