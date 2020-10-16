from urllib.parse import urljoin
import requests
from pprint import pprint

# Insert token below:
TOKEN = ''
VERSION = '5.124'
API_BASE_URL = 'https://api.vk.com/method/'


class Vk_Friends:
    BASE_URL = API_BASE_URL

    def __init__(self, user_id, token=TOKEN, version=VERSION):
        self.token = token
        self.user_id = user_id
        self.version = version

    def __str__(self):
        link = urljoin('https://vk.com/', 'id'+str(self.user_id))
        return link

    def __and__(self, other):

        mutual_friends_url = urljoin(API_BASE_URL, 'friends.getMutual')
        result = requests.get(mutual_friends_url, params={
            'source_uid': self.user_id,
            'target_uid': other.user_id,
            'access_token': self.token,
            'v': self.version
        })
        common_friends = []
        for friend in result.json()['response']:
            common_friends.append(Vk_Friends(friend))

        return common_friends


if __name__ == '__main__':
    user_1 = Vk_Friends(5725533)
    user_2 = Vk_Friends(132004061)
    user_3 = Vk_Friends(270166413)

    a = user_3 & user_2
    b = a[1] & user_2

    print(user_2)
    print(user_3)
    print(b[1])
