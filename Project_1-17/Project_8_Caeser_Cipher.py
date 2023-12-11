# encoding and decoding messages

from pic_art import caeser_cipher
print(caeser_cipher)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caeser(plain_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= (-1)
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter                      # for spaces and special charactrers
    print(f"The {cipher_direction}d text is {end_text}\n")




asking = True
while asking:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
    text = input("Type your message:").lower()
    shift = int(input("Type the shift number:"))
    shift %= 26
    caeser(plain_text=text,shift_amount=shift,cipher_direction=direction)

    asking = input("Type 'yes' if you want to do it again, otherwise 'no' : ").lower()
    if asking == 'no':
        asking = False
        print("Goodbye!")
