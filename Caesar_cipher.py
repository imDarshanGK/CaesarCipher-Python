alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char.lower() in alphabet:  # Check lowercase version of the character
            is_upper = char.isupper()  # Check if the original character is uppercase
            position = alphabet.index(char.lower())
            new_position = (position + shift_key) % 26
            new_char = alphabet[new_position]
            cipher_text += new_char.upper() if is_upper else new_char  # Preserve original case
        else:
            cipher_text += char  # Non-alphabet characters remain unchanged
    print(f"Here's the text after encryption: {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char.lower() in alphabet:  # Check lowercase version of the character
            is_upper = char.isupper()  # Check if the original character is uppercase
            position = alphabet.index(char.lower())
            new_position = (position - shift_key) % 26
            new_char = alphabet[new_position]
            plain_text += new_char.upper() if is_upper else new_char  # Preserve original case
        else:
            plain_text += char  # Non-alphabet characters remain unchanged
    print(f"Here's the text after decryption: {plain_text}")

end_program = False
while not end_program:
    what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n").lower()
    text = input("Type your message:\n")  # No longer forcing lowercase here
    shift = int(input("Enter shift key:\n"))
    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif what_to_do == "decrypt":
        decryption(cipher_text=text, shift_key=shift)
    else:
        print("Invalid option. Please type 'encrypt' or 'decrypt'.")
    play_again = input("Type 'yes' to continue, type 'no' to exit.\n").lower()
    if play_again == 'no':
        end_program = True
        print("Have a nice day!!")