from enum import Enum


class ActionType(Enum):
    NEW_MESSAGE = 4
    FRIEND_ONLINE = 8
    FRIEND_OFFLINE = 9


class ExtraFields(Enum):
    UNREAD = 0
    OUTBOX = 1
    REPLIED = 2
    IMPORTANT = 3
    CHAT = 4
    FRIENDS = 5
    SPAM = 6
    DELЕTЕD = 7
    FIXED = 8
    MEDIA = 9
    HIDDEN = 16
    DELETE_FOR_ALL = 17
    NOT_DELIVERED = 18
