import json
from dataclasses import dataclass, asdict


@dataclass
class UserModel:
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

    def to_dict(self) -> dict:
        return asdict(self)
