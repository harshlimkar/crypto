import json
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256

def pad(data):
    pad_length = 16 - len(data) % 16
    return data + bytes([pad_length]) * pad_length

def unpad(data):
    return data[:-data[-1]]

def encrypt_message(message):
    key = get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    hash_obj = SHA256.new(message.encode())
    message_hash = hash_obj.hexdigest()

    ciphertext = cipher.encrypt(pad(message.encode()))

    payload = {
        "key": base64.b64encode(key).decode(),
        "iv": base64.b64encode(iv).decode(),
        "hash": message_hash,
        "ciphertext": base64.b64encode(ciphertext).decode()
    }

    return json.dumps(payload), payload

def decrypt_message(payload_json):
    payload = json.loads(payload_json)

    key = base64.b64decode(payload["key"])
    iv = base64.b64decode(payload["iv"])
    ciphertext = base64.b64decode(payload["ciphertext"])
    original_hash = payload["hash"]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext)).decode()

    new_hash = SHA256.new(decrypted.encode()).hexdigest()

    return decrypted, new_hash == original_hash
