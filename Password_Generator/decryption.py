from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import art
import sys
import menu_prompt
import return_to_menu

#PRIVATE KEY IMPORT
def pwd_decryption():
	art.tprint('''\nZPD\n''', font='isometric1')
	print('Zorkol Password Decryptor'.center(43))
	#Importing keys from files, converting it into the RsaKey object  
	private_decrypt_key = False
	while not private_decrypt_key:
		try:
			private_decrypt_key = input('\nPrivate Key File Name >> ') 
			pr_key = RSA.import_key(open(private_decrypt_key, 'r').read())
			decryption = PKCS1_OAEP.new(key=pr_key)
			decryptor(decryption)
		except (FileNotFoundError, ValueError):
			print('''\nPossible errors:
Private key or password file doesn\'t exist.
Private key bits are not enough for encryption (please select ZH from the menu for more information about encryption).''')
			private_decrypt_key = False
		except KeyboardInterrupt:
			print('\n')
			return_to_menu.back_to_menu()

#PASSWORD DECRYPTOR
def decryptor(decryption):
	file_to_decrypt = False
	while not file_to_decrypt:
		file_to_decrypt = input('\nFile to decrypt >> ')
		decrypted_file = open(file_to_decrypt, 'rb').read() #Write down name of file
		decrypted_passwords = decryption.decrypt(decrypted_file).decode('utf-8')
		decrypted_pwd_file_creation(decrypted_passwords)
		
#DECRYPTED PASSWORD FILE CREATION/EXPORT
def decrypted_pwd_file_creation(decrypted_passwords):
	new_file = False
	while not new_file:
		try:
			new_file = input('\nNew file name >> (Do not include \'.txt\') ')
			with open(new_file + '.txt', 'w') as pl: 
				pl.write(''.join(decrypted_passwords)) 
				pl.close()
				print('\nFile has been exported.\n') 
				return_to_menu.back_to_menu()	
		except ValueError:
			print('Check your spelling')
			new_file = False




