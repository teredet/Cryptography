def сaesar_сiplet(menu, message, key):
    '''
    menu - 'E' if you want to encrypt and 'D' if you want to decrypt\n
    message - the string to encode or decore\n
    key - the number to shift\n
    \n
    The function encodes or decodes the message.\n
    Returns a string.\n
    
    '''
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    message = message.upper()
    key = int(key)
    output = ''
    
    if menu == 'D':
        key *= -1
    for letter in message:
        if letter in alphabet:
            t = alphabet.find(letter)
            new_key = (t + key) % len(alphabet)
            output += alphabet[new_key]
        else:
            output += letter
    return output