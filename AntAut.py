letters ='abcdefghijklmnopqrstuvwxyz'

def crypting(n, plaintext):
	letter=''

	for l in plaintext:
		try:	
			i =(letters.index(l) + int(n)) % 26
			letter += letters[i]
		except ValueError:
			letter += l
	return letter


def decrypting(n, ciphertext):
	letter = ''

	for l in ciphertext:
		try:
			i = (letters.index(l) - int(n)) % 26
			letter += letters[i]
		except ValueError:
			letter += l
	return letter

tradText = input("Your text : ")
offset = input("Offset : ")

crypter = crypting(offset, tradText)
print('Crypted message : ', crypter)

decrypter = decrypting(offset, crypter)
print('Decrypted message: ', decrypter)