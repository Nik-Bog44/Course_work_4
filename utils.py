import hashlib

import jwt
from flask import request

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


def auth_required(fun):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return '', 401
        data = request.headers['Authorization']
        token = data.split('Beare ')[-1]
        try:
            jwt.decode(token, PWD_HASH_SALT, algorithms=['H256'])
        except Exception as e:
            return ('JWT Decode error'), 401
        return fun(*args, **kwargs)

    return wrapper


def admin_required(fun):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return '', 401
        data = request.headers['Authorization']
        token = data.split('Beare ')[-1]
        role = None
        try:
            decode_token = jwt.decode(token, PWD_HASH_SALT, algorithms=['H256'])
            role = decode_token.get('role')
        except Exception as e:
            return ('JWT Decode error'), 401
        if role != 'admin':
            return "", 403
        return fun(*args, **kwargs)

    return wrapper


def get_hash(password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
