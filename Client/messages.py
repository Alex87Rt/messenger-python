from dataclasses import dataclass


@dataclass
class Authenticate:
    account_name: str
    password: str
