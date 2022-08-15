from typing import Optional

import requests
from config import VkUser
from requests import Response
from settings import *


class VkRequestsHandler:

    def __init__(self, user: VkUser):
        self.__messages = MessagesRequests(user)
        self.__longpoll = LongpollRequests(user)

    def messages(self) -> "MessagesRequests":
        return self.__messages

    def longpoll(self) -> "LongpollRequests":
        return self.__longpoll


class VkRequestsBase:

    def post(self, url: str, **kwargs) -> Optional[Response]:
        r = requests.post(url, **kwargs)
        if not self.__is_ok(r):
            return None
        return r

    def get(self, url: str, **kwargs) -> Optional[Response]:
        r = requests.get(url, **kwargs)
        if not self.__is_ok(r):
            return None
        return r

    def __is_ok(self, request: Response) -> bool:
        return request.ok


class MessagesRequests(VkRequestsBase):

    def __init__(self, user: VkUser):
        self.user = user

    def send(self, user_id: str, message: str):
        params_ = {
            "access_token": self.user.access_token,
            "user_id": user_id,
            "random_id": 0,
            "message": message,
            "v": VK_API_VERSION,
        }
        r = self.get(f"{VK_API_METHOD}/messages.send", params=params_).json()
        print(r)
        return r["response"]

    def get_conversations(self):
        params_ = {
            "access_token": self.user.access_token,
            "v": VK_API_VERSION,
        }
        r = self.get(f"{VK_API_METHOD}/messages.getConversations", params=params_).json()
        return r["response"]

    def get_longpoll_server(self):
        params_ = {
            "access_token": self.user.access_token,
            "v": VK_API_VERSION,
        }
        r = self.get(f"{VK_API_METHOD}/messages.getLongPollServer", params=params_).json()
        return r["response"]


class LongpollRequests(VkRequestsBase):

    def __init__(self, user: VkUser):
        self.user = user

    def send_longpoll_query(self, user: VkUser, server: str, key: str, ts: int):
        link = f"{HTTPS}{server}"
        params_ = {
            "act": "a_check",
            "key": key,
            "ts": ts,
            "wait": WAIT_LONGPOLL_TIMEOUT,
            "version": 10,
        }
        r = requests.post(link, params=params_).json()
        return r
