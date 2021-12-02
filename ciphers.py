from random import choice

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


def homophonic_substitution_cipher(mode, message, key):
	'''
	mode - 'E' if you want to encrypt and 'D' if you want to decrypt\n
	message - the string to encode or decore\n
	\n
	The function encodes or decodes the message.\n
	Returns a string.\n    
	'''
	
	final = ""

	values = ['1','2','3','4','5','6','7','8','9','0','a','b','c',\
	'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',\
	't','u','v','w','x','y','z','!','@','\\','#','№','$',';','%','^',\
	':','&','?','(',')','-','_','+','=','`','~','[',']','{',\
	'}','.',',','/','|','A','B','C','D','E','F','G','H','J','K','L',\
	'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','<',\
	'>','А','М','В','С','у','Е','Т','а','Х','Й']

	dictHom = {
		'A':values[0:8],	'B':values[8:10],
		'C':values[10:13],	'D':values[13:17],
		'E':values[17:29],	'F':values[29:31],
		'G':values[31:33],	'H':values[33:39],
		'I':values[39:45],	'J':[values[45]],
		'K':[values[46]],	'L':values[47:51],
		'M':values[51:53],	'N':values[53:59],
		'O':values[59:66],	'P':values[66:68],
		'Q':[values[68]],	'R':values[69:75],
		'S':values[75:81],	'T':values[81:90],
		'U':values[90:93],	'V':[values[93]],
		'W':values[94:96],	'X':[values[96]],
		'Y':values[97:99],	'Z':[values[99]],
		' ':[values[100]]
	}

	if mode == 'E':
		for symbol in message.upper():
			if symbol in dictHom:
				final += choice(dictHom[symbol])
	elif mode == 'D':
		for symbol in message:
			for key in dictHom:
				if symbol in dictHom[key]:
					final += key

	return final