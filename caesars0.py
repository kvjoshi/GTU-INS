
mode = str(raw_input("Do you want to encrypt or decrypt ?"))
message = str(raw_input("Input the message : "))
key = int(raw_input("Enter the key : "))
translated = ''
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
if message.isupper():
            alp = 1
            message = message.lower()
else:
    alp =0


for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)


        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key



        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:

        translated = translated + symbol

print("Your Translated text is : ")
if alp == 1 :
    print(translated.upper())
else:
    print(translated)

