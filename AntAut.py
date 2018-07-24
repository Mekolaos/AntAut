lettres ='abcdefghijklmnopqrstuvwxyz'

def crypteur(n, plaintext):
	lettre=''

	for l in plaintext:
		try:	
			i =(lettres.index(l) + int(n)) % 26
			lettre += lettres[i]
		except ValueError:
			lettre += l
	return lettre


def decrypteur(n, ciphertext):
	lettre = ''

	for l in ciphertext:
		try:
			i = (lettres.index(l) - int(n)) % 26
			lettre += lettres[i]
		except ValueError:
			lettre += l
	return lettre

tradTexte = input("Votre texte : ")
decalage = input("Décalage de : ")

crypter = crypteur(decalage, tradTexte)
print('Message crypté : ', crypter)

decrypter = decrypteur(decalage, crypter)
print('Décrypté : ', decrypter)