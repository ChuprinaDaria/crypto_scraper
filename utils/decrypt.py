from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import json
import binascii
import hashlib

def evp_kdf(password, salt, key_size=32, iv_size=16):
    derived = b""
    block = None
    while len(derived) < key_size + iv_size:
        hasher = hashlib.md5()
        if block:
            hasher.update(block)
        hasher.update(password)
        hasher.update(salt)
        block = hasher.digest()
        derived += block
    return derived[:key_size], derived[key_size:key_size + iv_size]

def decrypt_cryptojs_aes_json(encrypted_json_str, password):
    data = json.loads(encrypted_json_str)

    ct = base64.b64decode(data['ct'])
    salt = binascii.unhexlify(data['s'])
    iv = binascii.unhexlify(data['iv'])

    key, _iv = evp_kdf(password.encode(), salt)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ct), AES.block_size)
    return decrypted.decode('utf-8').replace('\\/', '/').replace('"', '')

