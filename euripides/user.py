import vk_api
from config import token

session = vk_api.VkApi(token=token) # Check config.py
vk = session.get_api()


class User():

    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def get_user_friends(user_id):
        """
        Get first user_ids of specific user
        :param user_id:
        :return: status {count, [user_id*]}
        """
        params = {
            'user_id': user_id
        }
        status = session.method("friends.get", params)
        return status

    def friends(self):
        """
        Getting user_ids of our first user_ids
        :return:
        """
        data = self.get_user_friends(self.user_id)
        for friends_id in data['items']:
            yield self.get_user_friends(friends_id)['items']
