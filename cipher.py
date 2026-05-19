def encrypt(message, k):
    result = ""
    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            p = ord(char) - shift
            encrypted_char = chr((p + k) % 26 + shift)
            result += encrypted_char
        else:
            result += char
    return result


def decrypt(message, k):
    result = ""
    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            p = ord(char) - shift
            decrypted_char = chr((p - k) % 26 + shift)
            result += decrypted_char
        else:
            result += char
    return result


# MAIN PROGRAM
k = 3  # shift value

user_input = input("Enter a message: ")

encrypted = encrypt(user_input, k)
print(f"The user input a message {user_input}, by encrypting with shift cipher, the corresponding Encrypted message is {encrypted}")

decrypted = decrypt(encrypted, k)
print(f"The encrypted message is {encrypted}, by decrypting with shift cipher, the corresponding Decrypted message is {decrypted}")
