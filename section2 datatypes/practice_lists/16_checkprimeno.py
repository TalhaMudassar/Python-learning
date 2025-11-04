from collections import Counter

cipher_text = "SDS CXOFOB DOY VKDO DOY LO GRKD IYE WSQRD RKFO LOOX"

# Step 1: Count frequency of letters
letters_only = [c for c in cipher_text if c.isalpha()]
freq = Counter(letters_only)
most_common_letter = freq.most_common(1)[0][0]

# Step 2: Assume most frequent ciphertext letter = 'E'
key = (ord(most_common_letter) - ord('E')) % 26
print("Most frequent letter:", most_common_letter)
print("Estimated key:", key)

# Step 3: Decrypt using that key
def decrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            result += char
    return result

plaintext = decrypt_caesar(cipher_text, key)
print("Decrypted text:", plaintext)
