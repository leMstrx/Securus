from cryptography.fernet import Fernet

# Generate a key for encryption (this should be kept secret)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(password.encode())

def decrypt_password(key, encrypted_password):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_password).decode()

def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data
