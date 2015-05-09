import os
import sys
import unittest

base_appdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_appdir not in sys.path:
    sys.path.append(base_appdir)
import a2r_app       # noqa


class A2RTestCase(unittest.TestCase):
    def setUp(self):
        a2r_app.app.config['TESTING'] = True
        a2r_app.app.config['WTF_CSRF_ENABLED'] = False
        self.app = a2r_app.app.test_client()

    def test_conversions(self):
        for number in benchmarks.keys():
            payload = {'num': number}
            rv = self.app.post('/arabic2roman', data=payload)
            assert benchmarks[number] in rv.data


benchmarks = {
    6: 'VI',
    9: 'IX',
    18: 'XVIII',
    19: 'XIX',
    38: 'XXXVIII',
    39: 'XXXIX',
    40: 'XL',
    98: 'XCVIII',
    388: 'CCCLXXXVIII',
    499: 'CDXCIX',
    867: 'DCCCLXVII',
    1998: 'MCMXCVIII',
    3999: 'MMMCMXCIX',
}


if __name__ == "__main__":
    unittest.main()
