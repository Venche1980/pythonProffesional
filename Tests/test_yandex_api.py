import unittest
import requests


class TestYandexDisk(unittest.TestCase):
    def setUp(self):
        self.token = ''  # Здесь нужно вставить ваш токен
        self.url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        self.folder_name = "test_folder"

    def test_create_folder_success(self):
        """Тест на успешное создание папки"""
        params = {"path": self.folder_name}
        response = requests.put(self.url, headers=self.headers, params=params)
        self.assertEqual(response.status_code, 201)

    def test_folder_exists(self):
        """Тест на проверку наличия созданной папки"""
        params = {"path": self.folder_name}
        response = requests.get(self.url, headers=self.headers, params=params)
        self.assertEqual(response.status_code, 200)

    def test_create_folder_error(self):
        """Тест на создание папки с неправильным токеном"""
        bad_headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth wrong_token'
        }
        params = {"path": self.folder_name}
        response = requests.put(self.url, headers=bad_headers, params=params)
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()