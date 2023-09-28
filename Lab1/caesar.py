def caesar_cipher(text, shift, operation, alphabet):
    text = text.upper()
    text = text.replace(' ', '')
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if operation == "encrypt":
                new_index = (index + shift) % 26
            else:
                new_index = (index - shift) % 26
            encrypted_text += alphabet[new_index]
        else:
            print(f"The character '{char}' is not allowed. Please use only the letters 'A'-'Z' or 'a'-'z'.")
            return

    return encrypted_text


def caesar_cipher_extended(text, shift, key, operation, alphabet):
    key = remove_duplicates(key)
    modified_alphabet = rotate_left(remove_duplicates((key + alphabet).upper()), shift)
    print('Modified alphabet')
    print(modified_alphabet)
    return caesar_cipher(text, shift, operation, modified_alphabet)


def remove_duplicates(input_string):
    output_string = ""
    for char in input_string:
        if char not in output_string:
            output_string += char
    return output_string


def rotate_left(input_string, n):
    n = n % len(input_string)
    return input_string[n:] + input_string[:n]

def menu(input_number):
    if input_number == 1:
        print(caesar_cipher(enc_mess, 3, operations[0], alphabet))
        exit()
    elif input_number == 2:
        print(caesar_cipher(dec_mess, 3, operations[1], alphabet))
        exit()
    elif input_number == 3:
        print(caesar_cipher_extended(enc_mess, 3, key, operations[0], alphabet))
        exit()
    else:
        print(caesar_cipher_extended(dec_mess, 1, key, operations[1], alphabet))
        exit()

# Test cases
if __name__ == "__main__":
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    operations = ['encrypt', 'decrypt']
    enc_mess = input("Message to be encrypted : ")
    dec_mess = input("Message to be decrypted : ")
    key = input("Input secret key : ")
    i = input("What fo you wnat to do? ")
    i = int(i)
    print(menu(i))
