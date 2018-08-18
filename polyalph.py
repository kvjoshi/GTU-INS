base = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

mode = raw_input("Do you want to encrypt or decrypt")
text = raw_input("Please enter the text")
key = raw_input("Please enter the key word")
keyList = []
keyLength = 0

while keyLength < len(text):
    for char in key:
        if keyLength < len(text):
            keyList.append(str(char))
            keyLength = keyLength + 1

ctext = []
cipherCharIndexValue = 0
keyinc = 0
textChar = []
ctextChar = []
if mode == "encrypt":
    for textChar in text:
        cipherCharIndexValue = base.index(keyList[keyinc]) + base.index(textChar)
        while cipherCharIndexValue > 25:
            cipherCharIndexValue = cipherCharIndexValue - 26
        ctext.append(base[cipherCharIndexValue])
        keyinc = keyinc + 1
    print (''.join(ctext))
if mode == "decrypt":
    for textChar in text:
        cipherCharIndexValue = base.index(textChar) - base.index(keyList[keyinc])
        while cipherCharIndexValue > 25:
            cipherCharIndexValue = cipherCharIndexValue - 26
        ctext.append(base[cipherCharIndexValue])
        keyinc = keyinc + 1
    print (''.join(ctext))
