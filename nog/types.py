from __future__ import annotations

import dataclasses
import logging
from typing import Any, Dict, List, Optional


@dataclasses.dataclass
class TextMetadata:
    title: str
    subtitle: str
    authors: List[str]
    categories: List[str]
    description: str
    published_date: str
    identifiers: List[Dict[str, str]]
    thumbnail: str
    language: str
    publisher: Optional[str] = None

    @classmethod
    def from_google_books_result(cls, response: Dict[str, Any]) -> TextMetadata:
        n_items = response['totalItems']
        if n_items == 0:
            raise ValueError(f"No items returned from response.")
        if n_items > 1:
            logging.warning(f"Reponse has {response['totalItems']} total items. Taking the first.")
        info = response['items'][0]['volumeInfo']
        return cls(title=info["title"],
                   subtitle=info["subtitle"],
                   authors=info["authors"],
                   description=info["description"],
                   categories=info["categories"],
                   publisher=info.get("publisher"),
                   published_date=info["publishedDate"],
                   identifiers=info["industryIdentifiers"],
                   thumbnail=info["imageLinks"]["thumbnail"],
                   language=info["language"])
