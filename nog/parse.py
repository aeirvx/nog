import io
import re
import sys
from typing import List

import requests
from pdfminer import high_level as pdf

from .types import TextMetadata


def parse_url(url: str) -> TextMetadata:
    content = requests.get(url, stream=True)
    content.raise_for_status()
    byts = content.content
    if not byts.startswith(b"%PDF"):
        raise ValueError(f"Could not parse file as a PDF.")
    return get_metadata_for_pdf(byts)


def get_metadata_for_pdf(pdf_bytes: bytes,
                         query_url: str = "https://www.googleapis.com/books/v1/volumes?q=isbn:",
                         first_n_pages: int = 5) -> TextMetadata:

    text = pdf.extract_text(io.BytesIO(pdf_bytes), maxpages=first_n_pages)
    isbns = get_isbns(text)

    for isbn in isbns:
        try:
            gbooks_response = requests.get(f"{query_url}{isbn}")
            gbooks_response.raise_for_status()
        except:
            continue
        return TextMetadata.from_google_books_result(gbooks_response.json())
    raise ValueError(f"Could not find a valid ISBN.")


def get_isbns(text: str, isbn_regex: re.Pattern = re.compile("(?:\d[\d\- ]{8,15}[\d|X])")) -> List[str]:
    candidates = re.findall(isbn_regex, text)
    filtered_candidates = [candidate for candidate in candidates if validate_isbn(candidate)]
    return filtered_candidates


def validate_isbn(isbn: str) -> bool:
    last = isbn[-1]
    if last.isdigit():
        last = int(last)
    elif last == "X":
        last = "X"
    else:
        return False

    digits = [int(c) for c in isbn[:-1] if c.isdigit()]
    if len(digits) == 9:
        val = sum((x + 2) * y for x, y in enumerate(reversed(digits)))
        check = 11 - (val % 11)
        if check == 10 and last == "X":
            return True
        if check == 11 and last == 0:
            return True
        return check == last

    elif len(digits) == 12:
        val = sum((x % 2 * 2 + 1) * int(y) for x, y in enumerate(digits))
        check = 10 - (val % 10)
        return check == last

    else:
        return False
