class VigenereCipher:
    def __init__(self):
        pass
    
    def vigenere_encrypt(self, plaintext, key):
        encrypted_text = ""
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text
    
    def vigenere_decrypt(self, ciphertext, key):
        decrypted_text = ""
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text
    