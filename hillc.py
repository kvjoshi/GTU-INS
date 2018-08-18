from string import join
from numpy import matrix
from numpy import linalg
from math import sqrt

def hill(message, key):

    n = int(sqrt(len(key)))
    if n * n != len(key):
        raise Exception("Invalid key length, should be square-root-able like")

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print "[ALPHA LENGTH]: ", len(alpha)
    tonum = dict([(alpha[i], i * 1) for i in range(len(alpha))])


    if len(message) % n > 0:
        message += 'X' * (n - (len(message) % n)) #pad if mod not=0


    keylist = []
    for a in key:
        keylist.append(tonum[a])    #matrix baniu

    keymatrix = []
    for i in range(n):
        keymatrix.append(keylist[i * n : i * n + n])

    keymatrix = matrix(keymatrix).round().T
    print(keylist)
    if mode=='decrypt':
        determinant = linalg.det(keymatrix).round()
        print "[DETERMINANT]", determinant
        if determinant == 0:
            raise Exception("Determinant ZERO, CHANGE THE KEY!")
        elif determinant % len(alpha) == 0:
            raise Exception("Determinant divisible by ALPHA LENGTH, CHANGE THE KEY!")

        inverse = []
        keymatrix =  matrix(keymatrix.getI() * determinant).round()

        invdeterminant = 0
        for i in range(10000):
            if (determinant * i % len(alpha)) == 1:
                invdeterminant = i
                break

        print "[INVERTED DETERMINANT]", invdeterminant


        for row in keymatrix.getA() * invdeterminant:
            newrow = []
            for i in row:
                newrow.append( i.round() % len(alpha) )
            inverse.append(newrow)          #mult inv

        keymatrix = matrix(inverse)

        print "[DECIPHERING]: ", message
    else:
      print "[ENCIPHERING]: ", message

    print "[MATRIX]\n", keymatrix

    # Main loop

    out = ''
    for i in range(len(message) / n):
        lst = matrix( [[tonum[a]] for a in message[i * n:i * n + n]] )
        result = keymatrix * lst
        out += ''.join([alpha[int(result.A[j][0]) % len(alpha)] for j in range(len(result))])

    return out
mode= raw_input("please enter encrypt or decrypt")
key = raw_input("please enter key")
msg = raw_input("Please enter the message")
if mode=='encrypt':
    cipherText = hill(msg, key)
    print "[CIPHERED TEXT]: |%s|\n" % cipherText
if mode=='decrypt':
    decipherText = hill(msg, key)
    if decipherText.find('|') > -1 : decipherText = decipherText[:decipherText.find('|')]
    print "[DECIPHERED TEXT]: |%s|\n" % decipherText
