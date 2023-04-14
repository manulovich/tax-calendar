import json
import random
from .store import Store

"""
[
    {
        "autor": "Name Lastame",
        "quote": "Lorem ipsum"
    },
    ...
]
"""


class QuotesStore(Store):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.quotes = json.load(file)

    def get_random_quote(self) -> str:
        quote = random.choice(self.quotes)

        return f'"{quote["quote"]}" - {quote["autor"]}'
