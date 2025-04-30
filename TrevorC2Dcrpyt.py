import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

# Constants
CIPHER_KEY = "Tr3v0rC2R0x@nd1s@w350m3#TrevorForget"

# Helper functions
def str_to_bytes(data):
    if isinstance(data, str):
        return data.encode('utf-8')
    return data

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

# AES decryption function
def decrypt(ciphertext_b64, key):
    try:
        key = hashlib.sha256(str_to_bytes(key)).digest()
        ciphertext_b64 = ciphertext_b64.strip()
        ciphertext_b64 += '=' * (-len(ciphertext_b64) % 4)

        enc = base64.b64decode(ciphertext_b64)
    except Exception as e:
        raise ValueError(f"Base64 decoding error: {e}")

    try:
        iv = enc[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(enc[AES.block_size:])
        plaintext = unpad(decrypted).decode('utf-8')
        return plaintext
    except Exception as e:
        raise ValueError(f"AES decryption error: {e}")

# Main function
if __name__ == "__main__":
    print("TrevorC2 Decryptor (Loop Mode)")
    print("--------------------------------\n")

    while True:
        encrypted_css = input("Enter base64 string to decrypt: ").strip()

        if not encrypted_css:
            print("[-] Empty input. Try again.\n")
            continue

        try:
            plaintext = decrypt(encrypted_css, CIPHER_KEY)
            print("\n[+] Decrypted content:")
            print(plaintext)
        except Exception as e:
            print(f"[-] Error: {e}")

        # Ask if the user wants to quit or continue
        next_action = input("\nPress Enter to decrypt another, or 'q' to quit: ").strip().lower()
        if next_action == 'q':
            print("\nGoodbye.")
            break

        print("\n--- New decryption round ---\n")
