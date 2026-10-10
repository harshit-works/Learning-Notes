import hashlib
txt = input("Enter the password")
# txt.encode()
hash_MD5 = hashlib.md5(txt.encode())
hash_sha256 = hashlib.sha256(txt.encode())

print ("\nmd5 hash =")
print(hash_MD5.hexdigest())
print ("\nsha256 hash =")
print(hash_sha256.hexdigest())



