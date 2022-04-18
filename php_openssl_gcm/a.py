import requests
import base64
from urllib.parse import urlparse, parse_qs, urlencode
from Crypto.Util.strxor import strxor

message = b"message to be encrypted"
target =  b"rewrited by kurenaif :)"

for i in range(3000):
    r = requests.get("http://localhost:8000/encrypt.php")
    r = parse_qs(urlparse(r.text).query)
    ciphertext = r['ciphertext'][0]
    tag = r['tag'][0]
    iv = r['iv'][0]
    print(ciphertext, tag, iv)

    ciphertext = base64.urlsafe_b64decode(ciphertext + '=' * (-len(ciphertext) % 4))
    tag = base64.urlsafe_b64decode(tag + '=' * (-len(tag) % 4))
    iv = base64.urlsafe_b64decode(iv+ '=' * (-len(iv) % 4))

    ciphertext = strxor(strxor(ciphertext, message), target)
    tag = tag[:1]

    ciphertext = base64.urlsafe_b64encode(ciphertext)
    tag = base64.urlsafe_b64encode(tag)
    iv = base64.urlsafe_b64encode(iv)

    query = urlencode({
        'ciphertext': ciphertext,
        'tag': tag,
        'iv': iv
    })

    r = requests.get("http://localhost:8000/decrypt.php?" + query)
    print(r.text)
