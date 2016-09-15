import hashlib

def generate(s):
    return hashlib.sha1(s).hexdigest()
