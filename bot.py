import vk_api

from config import VkUser
from Vk.queries import VkRequestsHandler
from Vk.longpoll import updates
from Vk.longpoll.updates import make_update_instance
from settings import ACCOUNT_PATH


def main():
    user = VkUser.from_json(ACCOUNT_PATH)
    session = vk_api.VkApi(token=user.access_token)

    req = VkRequestsHandler(user)
    data = req.messages().get_longpoll_server()

    while True:
        response = req.longpoll().send_longpoll_query(user, data["server"], data["key"], data["ts"])
        if "updates" in response:
            updates_ = response["updates"]
            for lst in updates_:
                event = make_update_instance(lst[0])
                if event:
                    event.update(lst, req)
        data["ts"] = response["ts"]


if __name__ == '__main__':
    main()
