#vigenere cipher


text = 'Hello Zebra'
key = 'meowmeowmeow'

def caeser_cipher(text, key):
    #encrypt
    final_message=''
    for char in text.lower():
        if not char.isalpha():
            final_message += char

        else:
            index = key.find(char)
            new_index = (index+key)%len(key)
            final_message += key[new_index]

    return final_message
        




print(caeser_cipher(text, key))