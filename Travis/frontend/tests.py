from django.test import TestCase

# Create your tests here.

class RandomTests(TestCase):

    def setUp(self):
        pass

    def test_pass(self):
        """This test should pass"""
        self.assertTrue(1 == 1)

    def test_fail(self):
        """This test should fail"""
        self.assertTrue(1 == 2)
