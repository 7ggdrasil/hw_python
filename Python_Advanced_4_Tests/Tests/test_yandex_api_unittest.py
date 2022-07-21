from yandex_upload import create_folder_Ya_API
import unittest
from unittest import TestCase


class TestYaAPI(TestCase):
    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    def test_create_folder_Ya_API(self):
        self.assertEqual(create_folder_Ya_API('test'), 201)

    @unittest.expectedFailure
    def test_expected_fail_create_folder_Ya_API(self):
        self.assertEqual(create_folder_Ya_API('test'), 409)
