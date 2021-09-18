# Nog

## Usage

See `tests/`.

```
from nog import parse

url = "https://libcom.org/files/David_Graeber-The_Utopia_of_Rules_On_Technology_St.pdf"
print(parse.parse_url(url))
>>> TextMetadata(title='The Utopia of Rules', subtitle='On Technology, Stupidity, and the Secret Joys of Bureaucracy', authors=['David Graeber'], categories=['Political Science'], description='Presents a tour through ancient and modern history to trace the evolution of bureaucracy while assessing the efficiencies and casualties of its practices in the modern world.', published_date='2015', identifiers=[{'type': 'ISBN_13', 'identifier': '9781612193748'}, {'type': 'ISBN_10', 'identifier': '1612193749'}], thumbnail='http://books.google.com/books/content?id=K8RvDwAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api', language='en', publisher='Melville House Publishing')
```