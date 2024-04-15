import requests
import unittest

class TestYandexDisk(unittest.TestCase):
    def setUp(self):
        self.headers = {'Authorization': 'y0_AgAAAABdAvPeAADLWwAAAAD5Dh-HAABMSZqFQTpOgaFMWbV63DM_Dgb-2w',
                        'Content-Type': 'application/json'}

    def test_creat_folder(self):
        params = {'path': 'Image102'}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources', headers=self.headers,
                                params=params)
        self.assertEqual(response.status_code, 201)



    def test_creat_folder_again(self):
        params = {'path': 'Image102'}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources', headers=self.headers,
                                params=params)
        self.assertEqual(response.status_code, 409)



    def test_create_folder_invalid_data(self):
        params = {'path': ''}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources', headers=self.headers,
                                params=params)
        self.assertEqual(response.status_code, 400)
    def test_unauthorized(self):
        headers = {'Content-Type': 'application/json'}  # Удаляем заголовок авторизации
        params = {'path': 'Image102'}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params=params)
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()