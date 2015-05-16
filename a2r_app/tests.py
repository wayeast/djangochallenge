from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class A2RTestCase(TestCase):
    def setUp(self):
        self.url = reverse('a2r_convert')
        self.client = Client()
        self.csrf_client = Client(enforce_csrf_checks=True)

    def test_csrf_enforcement(self):
        resp = self.csrf_client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        resp = self.csrf_client.post(self.url, {'num': '123'})
        self.assertEqual(resp.status_code, 403)

    def test_benchmarks(self):
        for key, value in benchmarks.items():
            resp = self.client.post(self.url, {'num': key})
            self.assertEqual(resp.status_code, 200)
            self.assertIn(value, resp.content)


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
