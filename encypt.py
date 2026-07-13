import os
from cryptography.fernet import Fernet



def create_key_path():
            key=Fernet.generate_key()
            with open("secure.key", "wb") as key_file:
                  key_file.write(key)


def encrypt_password(password):
      if not os.path.exists("secure.key"):
            create_key_path()
      with open("secure.key", "rb") as key:
            key=key.read()
      fernet=Fernet(key)
      print(fernet)
      encrypted=fernet.encrypt(password.encode())
      return encrypted


def decrypt_password(password):
      with open("secure.key", "rb") as key:
            pass_key=key.read()
            return pass_key.decrypt(password.encode)
      
password="man"
print(encrypt_password(password))
print(decrypt_password(password))
