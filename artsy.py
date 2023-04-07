import requests
import sys
import json
from operator import itemgetter

sys.stdin = open("artsy_in.txt", "r")

client_id = input()
client_secret = input()

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",  # инициируем запрос на получение токена
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)  # разбираем ответ сервера
token = j["token"]  # достаем токен
headers = {"X-Xapp-Token": token}  # создаем заголовок, содержащий наш токен

arts = []
with open("arts_id_in.txt", "r") as a:
    for art in a:
        art = art.rstrip()
        arts.append(art)
    print(arts)
data = []
d = {}
for i in range(len(arts)):
    r = requests.get(f"https://api.artsy.net/api/artists/{arts[i]}", headers=headers)  # инициируем запрос с заголовком
    j = json.loads(r.text)  # разбираем ответ сервера
    d[j['sortable_name']] = j['birthday']
    print(f'Processed {i + 1} names out of {len(arts)} - {j["sortable_name"]}!')

sorted_tuple = sorted(d.items(), key=itemgetter(1, 0))
d = dict(sorted_tuple)

with open("arts_out.txt", "w", encoding='UTF-8') as out:
    for i in d:
        out.write(i + '\n')
