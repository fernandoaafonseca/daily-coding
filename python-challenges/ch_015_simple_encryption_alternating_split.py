'''
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:
encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"

Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
'''


def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text

    for times in range(n):
        if times == 0:
            new_text = encrypted_text
        else:
            new_text = decrypted_text

        text_length = len(new_text)
        half_length = text_length // 2
        even_chars = new_text[half_length:]
        odd_chars = new_text[:half_length]

        decrypted_text = ''
        for i in range(half_length):
            decrypted_text += even_chars[i] + odd_chars[i]
        if text_length % 2 != 0:
            decrypted_text += even_chars[-1]

    return decrypted_text


def encrypt(text, n):
    if not text or n <= 0:
        return text

    for times in range(n):
        if times == 0:
            new_text = text
        else:
            new_text = encrypted_text

        encrypted_text = ''.join(new_text[i]
                                 for i in range(len(new_text)) if i % 2 != 0)
        encrypted_text += ''.join(new_text[i]
                                  for i in range(len(new_text)) if i % 2 == 0)

    return encrypted_text


print(encrypt('012345', 1))
print(decrypt('135024', 1))
print('=' * 20)

print(encrypt('012345', 2))
print(decrypt('304152', 2))
print('=' * 20)

print(encrypt('This is a test!', 3))
print(decrypt(' Tah itse sits!', 3))
print('=' * 20)

print(encrypt('This kata is very interesting!', 1))
print(decrypt('hskt svr neetn!Ti aai eyitrsig', 1))
print('=' * 20)
