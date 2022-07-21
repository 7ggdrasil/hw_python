from unittest import TestCase
from unittest import mock

from main import documents, directories
from main import get_user_name, get_dir, get_users, add_new_user, delete_acc, move_acc_to_new_dir


class TestAddNewUser(TestCase):
    @mock.patch('main.input', create=True)
    def test_add_new_user(self, mocked_input):
        mocked_input.side_effect = ['prava', '322', 'Solo', '3']
        expected_doc = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
                        {"type": "prava", "number": "322", "name": "Solo"}]
        expected_dir = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': ['322']}
        result = add_new_user(documents, directories)
        self.assertEqual(result, (expected_doc, expected_dir))


class TestDeleteAcc(TestCase):
    @mock.patch('main.input', create=True)
    def test_add_new_user(self, mocked_input):
        mocked_input.side_effect = ['322']
        expected_doc = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]
        expected_dir = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}
        result = delete_acc(documents, directories)
        self.assertEqual(result, (expected_doc, expected_dir))


class TestMoveAccToNewDir(TestCase):
    @mock.patch('main.input', create=True)
    def test_move_acc_to_new_dir(self, mocked_input):
        mocked_input.side_effect = ['11-2', '2']
        expected_dir = {'1': ['2207 876234'], '2': ['10006', '11-2'], '3': []}
        result = move_acc_to_new_dir(documents, directories)
        self.assertEqual(result, expected_dir)


class TestGetUserName(TestCase):
    @mock.patch('main.input', create=True)
    def test_get_user_name(self, mocked_input):
        mocked_input.side_effect = ['11-2']
        result = get_user_name(documents)
        self.assertEqual(result, 'Геннадий Покемонов')


class TestGetUserNameExpNoDoc(TestCase):
    @mock.patch('main.input', create=True)
    def test_get_user_name(self, mocked_input):
        mocked_input.side_effect = ['777']
        result = get_user_name(documents)
        self.assertEqual(result, 'Нет такой записи')


class TestGetDir(TestCase):
    @mock.patch('main.input', create=True)
    def test_get_dir(self, mocked_input):
        mocked_input.side_effect = ['11-2']
        result = get_dir(directories)
        self.assertEqual(result, '1')


class TestGetUsers(TestCase):
    def test_get_users(self):
        expected_result = [
            'passport "2207 876234" "Василий Гупкин"',
            'invoice "11-2" "Геннадий Покемонов"',
            'insurance "10006" "Аристарх Павлов"']
        self.assertListEqual(get_users(documents), expected_result)
