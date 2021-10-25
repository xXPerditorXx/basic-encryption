import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZäöüÄÖÜ1234567890!\"§$%&/()=?#'+*~\\}][{@€-_,;.:µ<>|^° "

in_put = input("Text to Encrypt: ")


def key_generation():
    enc_key = "".join(random.sample(letters, len(letters)))
    return enc_key


def encrypt(text, enc_key=key_generation()):
    enc_text = ""
    print(f"\nEncryption-Key: {enc_key}")
    for i in range(len(text)):
        encrypted = text[i].replace(text[i], enc_key[letters.index(text[i])])
        enc_text += encrypted
    return enc_text


def decrypt(text, dec_key):
    try:
        dec_text = ""
        for i in range(len(text)):
            decrypted = text[i].replace(dec_key[dec_key.index(text[i])], letters[dec_key.index(text[i])])
            dec_text += decrypted
        return dec_text
    except ValueError:
        print("Please use a Valid Key to decrypt.")
        exit(0)


abd = encrypt(in_put)
print(f"Encrypted: {abd}")
print(decrypt(abd, input("Key: ")))
