# ЗАДАЧА 1

import requests
import json

heroes_list = ['Hulk', 'Captain america', 'Thanos']
#создадим словарь, в котором будет находиться информация о интеллекте каждого героя (изначально 0)
intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

for hero in heroes_list:
    hero_dict = json.loads(requests.get(url + hero).content)
    for superhero in heroes_list:
        if superhero in heroes_list:
         intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])    
        hero, intelligence = max(intelligence_dict.items(), key=lambda x: x[1])    
        
print(f"Самый интелектуальный герой - {hero}, интелект: {intelligence}")






#ЗАДАЧА 2
    
# from pprint import pprint
# import requests

# TOKEN = '2619421814940190'  # константа токена

# class YandexDisk:

#     def __init__(self, token):
#         self.token = token

#     def get_headers(self):
#         return {
#             'Content-Type': 'application/json',
#             'Authorization': 'OAuth {}'.format(self.token)
#         }

#     def get_files_list(self):
#         files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
#         headers = self.get_headers()
#         response = requests.get(files_url, headers=headers)
#         return response.json()

#     def _get_upload_link(self, disk_file_path):
#         upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
#         headers = self.get_headers()
#         params = {"path": disk_file_path, "overwrite": "true"}
#         response = requests.get(upload_url, headers=headers, params=params)
#         pprint(response.json())
#         return response.json()

#     def upload_file_to_disk(self, disk_file_path, filename):
#         href_json = self._get_upload_link(disk_file_path=disk_file_path)
#         href = href_json["href"]
#         response = requests.put(href, data=open(filename, 'rb'))
#         response.raise_for_status()
#         if response.status_code == 201:
#             print("Успех")


# if __name__ == "__main__":
#     ya = YandexDisk(token=TOKEN)
#     ya.upload_file_to_disk('dik/test2.txt', 'test.txt')

















