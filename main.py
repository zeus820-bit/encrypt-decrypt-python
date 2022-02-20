char  = 'abcdefghijklmnopqrstuvwxyz'
print('1. Encrypt')
print('2. Decrypt')
opt = input('Enter E for encrypt or D for decrypt >>> ')

def encrypt():
    etext = []
    for i in text:
        x1 = char.find(i)
        x2 = char[x1+key]
        etext.append(x2)
    x3 = ''.join(etext)
    print('The encrypted message >>> ',x3)

def decrypt():
    dtext = []
    for j in text:
        x1 = char.find(j)
        x2 = char[x1-key]
        dtext.append(x2)
    x3 = ''.join(dtext)
    print('The decrypted message is >>> ',x3)
        

if opt == 'e':
    text = input('Enter the Message >>> ')
    key = int(input('Enter the key >>> '))
    encrypt()

elif opt == 'd':
    text = input('Enter the Message >>> ')
    key = int(input('Enter the key >>> '))
    decrypt()

else:
    print('Invalid Input')
