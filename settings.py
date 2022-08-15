import os


HTTPS = "https://"

VK_API = f"{HTTPS}api.vk.com"
VK_API_METHOD = f"{VK_API}/method"
VK_API_VERSION = 5.131

CFG_PATH = "cfg"
ACCOUNT_PATH = os.path.join(CFG_PATH, "account.json")

ERROR_REQUEST = "error"
RESPONSE_REQUEST = "response"

WAIT_LONGPOLL_TIMEOUT = 10
