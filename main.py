# Define a function to encrypt and decrypt text using XOR cipher
def xorCipher(input_text, key):
    # Convert the strings into bytes
    if isinstance(input_text, str):
        input_text = input_text.encode()

    if isinstance(key, str):
        key = key.encode()

    # Ensure the key is long enough to match the input text length
    if len(key) < len(input_text):
        key = key * (len(input_text) // len(key) + 1)
        key = key[:len(input_text)]

    # Perform XOR operation and return the result in bytes
    return bytes([a ^ b for a, b in zip(key, input_text)])


# Get user input for the message and the key
text = input("\nWhat's your secret message? ")
key = input("Enter the secret key for encryption: ")

# Encrypt the message
encrypted_msg = xorCipher(text, key)

print(f"\n🔒 Encrypted Message: {encrypted_msg}\n")

# Prompt user for decryption
print("Want to unlock the secret? Press (y or Y) to decrypt, or any other key to skip.")
ch = input("Do you want to decrypt the message? (y/n): ")

if ch == 'y' or ch == 'Y':
    # Decrypt the message
    decrypted_msg = xorCipher(encrypted_msg, key).decode()
    print(f"\n🔑 Key: {key}")
    print(f"🔓 Decrypted Message: {decrypted_msg}\n")
else:
    print("Decryption skipped. 🔐\n")
