# Function to generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved as secret.key")

# Function to load the key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a message
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

# Function to decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message)
    return decrypted.decode()

# Example usage
if _name_ == "_main_":
    print("1. Generate Key\n2. Encrypt Message\n3. Decrypt Message")
    choice = input("Choose an option: ")

    if choice == '1':
        generate_key()
    elif choice == '2':
        msg = input("Enter message to encrypt: ")
        encrypted_msg = encrypt_message(msg)
        print("Encrypted:", encrypted_msg)
    elif choice == '3':
        encrypted_input = input("Enter the encrypted message: ").encode()
        try:
            decrypted_msg = decrypt_message(encrypted_input)
            print("Decrypted:", decrypted_msg)
        except Exception as e:
            print("Error during decryption:", str(e))
    else:
        print("Invalid choice.")