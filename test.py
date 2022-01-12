import unittest
from reg import validate_number

class REtest(unittest.TestCase):

    def test_phone_validation_fail(self):
        phone = '99655555989923'
        result = validate_number(phone)
        self.assertEqual(result, False)

    def test_phone_validation_succes(self):
        phone = '996555559899'
        result = validate_number(phone)
        self.assertEqual(result, True)