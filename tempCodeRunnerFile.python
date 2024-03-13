# caeser cipher

text = 'Hello Zebra'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 3

def caeser_cipher(text, shift):
    #encrypt
    final_message=''
    for char in text.lower():
        if not char.isalpha():
            final_message += char

        else:
            index = alphabet.find(char)
            new_index = (index+shift)%len(alphabet)
            final_message += alphabet[new_index]

    return final_message
        




print(caeser_cipher(text, shift))