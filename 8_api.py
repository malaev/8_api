import requests
import json


def get_friends_by_user_id(user_id):
    response = requests.get('https://api.vk.com/method/friends.get?user_id=' + str(user_id) + '&fields=first_name&access_token=9c4a9c069c4a9c069c4a9c06849c23de6199c4a9c4a9c06c0c3aa704bf4b905e3eee7a9&v=5.52')
    try:
        friends_list = json.loads(response.text)["response"]["items"]
        return friends_list
    except:
        raise RuntimeError('Неверный или несуществующий id')


print('Введите id пользователя Вконтакте, чтобы получить список имен его друзей')
id = input()
friends = get_friends_by_user_id(id)

for friend in friends:
    print(friend["first_name"] + ' ' + friend["last_name"])
