def сaesar_сiplet(menu, message, key):
    '''
    menu - 'E' if you want to encrypt and 'D' if you want to decrypt\n
    message - the string to encode or decore\n
    key - the number to shift\n
    \n
    The function encodes or decodes the message.\n
    Returns a string.\n
    
    '''
    alphabetENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabetRU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    message = message.upper()
    key = int(key)
    output = ''
    
    if message[0] in alphabetENG:
        alphabet = alphabetENG
    elif message[0] in alphabetRU:
        alphabet = alphabetRU
    else:
        return 'Invalid message'

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

def vigenere_cipher(mode, message, key):
	'''
    mode - 'E' if you want to encrypt and 'D' if you want to decrypt\n
    message - the string to encode or decore\n
    key - codeword\n
    \n
    The function encodes or decodes the message.\n
    Returns a string.\n
	
	'''
	key *= len(message) // len(key) + 1  
	finalMessage = ""
	for i, j in enumerate(message):
		if mode == 'E':
			temp = ord(j) + ord(key[i])
		else:
			temp = ord(j) - ord(key[i])
		finalMessage += chr(temp % 26 + ord('A'))
	return finalMessage