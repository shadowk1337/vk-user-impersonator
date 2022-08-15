from Vk.longpoll.codes import ExtraFields


def is_user_message_id(peer_id: int) -> bool:
    return 0 <= peer_id < 2000000000


def is_outbox(flag: int) -> bool:
    return flag >> ExtraFields.OUTBOX.value & 1
