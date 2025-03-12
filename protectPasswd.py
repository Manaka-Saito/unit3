from passlib.context import CryptContext
from passlib.hash import sha256_crypt

hash_function = sha256_crypt.using(rounds = 30000)
pwd_config = CryptContext(schemes = ["sha256_crypt"],
                          default = "sha256_crypt")
def check_hash(input_str, hash):
    return pwd_config.verify(input_str, hash)

def encrypt_password(in_password:str):
    return pwd_config.hash(in_password)
