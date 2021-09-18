import pytest
from nog import parse


@pytest.mark.parametrize("url", [
    "https://cdn.discordapp.com/attachments/883440073473929307/886530475924008960/Braiding-Sweetgrass-Indigenous-Wisdom-Scientific-Knowledge-and-the-Teachings-of-Plants-PDFhive.com-1.pdf",
    "https://libcom.org/files/David_Graeber-The_Utopia_of_Rules_On_Technology_St.pdf"
])
def test_valid_urls(url):
    parse.parse_url(url)
