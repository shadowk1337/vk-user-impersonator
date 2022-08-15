import Vk.funcs as f

from Vk.longpoll.codes import ActionType, ExtraFields
from Vk.queries import VkRequestsHandler


class UpdateBase:

    def update(self, event_lst: list, req: VkRequestsHandler):
        raise NotImplementedError


class NewMessage(UpdateBase):

    def update(self, event_lst: list, req: VkRequestsHandler):
        flag, id = event_lst[2], event_lst[3]
        print(event_lst)
        if not f.is_outbox(flag) and f.is_user_message_id(id):
            req.messages().send(id, "TEST")


class FriendOnline(UpdateBase):

    def update(self, event_lst: list, req: VkRequestsHandler):
        pass


class FriendOffline(UpdateBase):

    def update(self, event_lst: list, req: VkRequestsHandler):
        pass


def make_update_instance(event_code: int) -> UpdateBase:
    if event_code == ActionType.NEW_MESSAGE.value:
        return NewMessage()
    elif event_code == ActionType.FRIEND_ONLINE.value:
        return FriendOnline()
    elif event_code == ActionType.FRIEND_OFFLINE.value:
        return FriendOffline()
