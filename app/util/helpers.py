import hashlib
from fastapi import Request

def hashcode(original_url: str) -> str:
    h = hashlib.shake_128(original_url.encode('utf-8'))
    return h.hexdigest(5)

def shortlink(request: Request, hashcode: str) -> str:
    return f"{str(request.base_url)}urls/{hashcode}"