monoalpha_cipher = {
    'a': 'X',
    'b': 'D',
    'c': 'G',
    'd': 'S',
    'e': 'Z',
    'f': 'A',
    'g': 'N',
    'h': 'Y',
    'i': 'O',
    'j': 'B',
    'k': 'T',
    'l': 'M',
    'm': 'J',
    'n': 'C',
    'o': 'E',
    'p': 'V',
    'q': 'F',
    'r': 'H',
    's': 'K',
    't': 'W',
    'u': 'P',
    'v': 'L',
    'w': 'Q',
    'x': 'U',
    'y': 'R',
    'z': 'I',
    ' ': ' ',
}
inverse_monoalpha_cipher = {}
for key, value in monoalpha_cipher.iteritems():
    inverse_monoalpha_cipher[value] = key
mode = raw_input("Do you want to Encrypt or Decrypt ?")
message = raw_input("Please enter the message : ")


if mode == "encrypt":
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter,letter))
    print(''.join(encrypted_message))

elif mode == "decrypt":
    decrypted_message = []
    for letter in message:
        decrypted_message.append( inverse_monoalpha_cipher.get(letter,letter))
    print(''.join( decrypted_message ))
