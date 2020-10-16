from urllib.parse import urljoin
import requests
from pprint import pprint

# insert your token below
TOKEN = ''
VERSION = '5.124'
API_BASE_URL = 'https://api.vk.com/method/'


class Vk_Friends:
    BASE_URL = API_BASE_URL

    def __init__(self, token=TOKEN, version=VERSION):
        self.token = token
        self.version = version

    def get_mutual_friends(self, other_id):
        mutual_friends_url = urljoin(API_BASE_URL, 'friends.getMutual')
        result = requests.get(mutual_friends_url, params={
            'target_uid': other_id,
            'access_token': self.token,
            'v': self.version
        })

        return result.json()['response']

if __name__ == '__main__':
    myself = Vk_Friends()
    pprint(myself.get_mutual_friends(372488475))