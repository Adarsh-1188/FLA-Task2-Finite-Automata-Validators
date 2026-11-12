import unittest
from fa_validators.validators import validate_pin, validate_password, validate_email

class TestATM_PIN(unittest.TestCase):
    def test_accepted(self):
        for value in ["1234", "0000", "5721", "2468", "9876"]:
            self.assertTrue(validate_pin(value), value)

    def test_rejected(self):
        for value in ["123", "12345", "12A4", "abcd", "12 4"]:
            self.assertFalse(validate_pin(value), value)

class TestPassword(unittest.TestCase):
    def test_accepted(self):
        for value in ["Abcd123!", "Strong9@", "A1b2c3$4", "Password1!", "Zx9#abcd"]:
            self.assertTrue(validate_password(value), value)

    def test_rejected(self):
        for value in ["abcdef12", "ABCDEFG!", "Abcdefgh", "Ab1!", "Abcd 123!"]:
            self.assertFalse(validate_password(value), value)

class TestEmail(unittest.TestCase):
    def test_accepted(self):
        for value in [
            "student@gmail.com", "a.b@college.edu", "user_123@test.org",
            "hello-world@example.co", "name@domain.in"
        ]:
            self.assertTrue(validate_email(value), value)

    def test_rejected(self):
        for value in [
            "studentgmail.com", "student@.com", "@gmail.com",
            "user@domain", "user@@gmail.com"
        ]:
            self.assertFalse(validate_email(value), value)

if __name__ == "__main__":
    unittest.main()
