from platform import platform
import random

def passwdGen():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '$', '#']

    characters = MAYUS + MINUS + NUMS + CHARS

    passwd = []

    for i in range(8):
        characters_random = random.choice(characters)
        passwd.append(characters_random)
    
    passwd = ''.join(passwd)
    return passwd

passwd = passwdGen()

def store():
    siteName = input('Nombre la plataforma o sitio web: ')
    passwdFile = open('passwds.txt','a')
    passwdFile.write('\n'+siteName+'\t\tY'+passwd)
    passwdFile.close

def run():
    userPasswd = passwd
    print('tu nueva contrasena es: ' + passwd)
    storePasswd = input('Almacenar contrasena(Y/N): ')
    if storePasswd == 'Y':
        store()
