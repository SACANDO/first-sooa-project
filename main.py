import hashlib

data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(b'test')
hex_dig = hash_object.hexdigest()
print(hex_dig)