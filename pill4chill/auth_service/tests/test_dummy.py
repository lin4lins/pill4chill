from rest_framework.test import APITestCase


class DummyTestCase(APITestCase):
    def test_none(self):
        self.assertEqual(True, True)
