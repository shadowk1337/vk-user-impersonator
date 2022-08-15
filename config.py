from dataclasses import dataclass
from typing import List
import json


@dataclass
class VkUser:
    access_token: str

    @classmethod
    def from_json(cls, file: str) -> "VkUser":
        with open(file, "rt") as f:
            j = json.loads(f.read())
        return VkUser(
            access_token=j["user"]["accessToken"]
        )
