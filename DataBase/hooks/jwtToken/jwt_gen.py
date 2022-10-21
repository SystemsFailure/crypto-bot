from time import time

import cryptography.exceptions
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_ssh_private_key
import jwt
import logging


payload_data = {
    'user_id': '13',
    "name": "Eric",
    'email': 'as@gmail.com'
}

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
log = logging.getLogger('my-logger')

# private_key = open('DataBase/hooks/jwtToken/id_ed25519', 'r').read()
# key = serialization.load_ssh_private_key(private_key.encode(), backend=default_backend(), password=b'31415')
key_default_virtual = 'secret'


class JWToken:
    @staticmethod
    def create_private_key():
        try:
            with open("my_key.pem", "rb") as key_file:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                    backend=default_backend()
                )
                return private_key
        except cryptography.exceptions.InvalidKey as ex:
            log.exception(f'{__name__}: {ex}')

    @staticmethod
    def create_public_key():
        try:
            with open("my_key.pem", "rb") as key_file:
                public_key = serialization.load_pem_public_key(
                    key_file.read(),
                    backend=default_backend()
                )
                return public_key
        except cryptography.exceptions.InvalidKey as ex:
            log.exception(f'{__name__}: {ex}')

    @staticmethod
    def encode_t():
        try:
            new_token = jwt.encode(payload=payload_data, key=key_default_virtual, algorithm='RS256')
            log.info(new_token)
            return new_token
        except jwt.exceptions.InvalidTokenError as ex:
            log.exception(ex)
            return False

    @staticmethod
    def decode_t(new_token, public_t: bytes = None, private_t: bytes = None):
        try:
            print(new_token)
            decode_jwt = jwt.decode(new_token, key=key_default_virtual, algorithms=['RS256', ])
            log.info(decode_jwt)
            return decode_jwt
        except jwt.InvalidSignatureError as ex:
            log.exception(ex)
            return False
            # exit(1)

