#ENCRYPTION WITH NEW KEYS
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from art import tprint
import return_to_menu
import sys

#PUBLIC KEY IMPORT
def pwd_encryption():
	tprint('''\nZPE\n''', font='isometric1')
	print('Zorkol Password Encryptor'.center(43))
	encryption_key = False
	while not encryption_key:	
		try:
			encryption_key = input('\nPublic Key File Name >> ')
			pu_key = RSA.import_key(open(encryption_key, 'r').read())
			encryption_key = PKCS1_OAEP.new(key=pu_key)
			encryptor(encryption_key)
		except (FileNotFoundError, ValueError):
			print('''\nPossible errors:
Public key or password file doesn\'t exist.
Public key bits are not enough for encryption (please select ZH from the menu for more information about encryption).''')
			encryption_key = False
		except KeyboardInterrupt:
			print('\n')
			return_to_menu.back_to_menu()

#PASSWORD ENCRYPTOR		
def encryptor(encryption_key):
	file_input = False
	while not file_input:
		pwd_file_to_list = [] 
		bytes_pwd_list = [] 
		file_input = input('\nFile to encrypt >> ')
		file_to_encrypt = open(file_input, 'r')
		for i in file_to_encrypt:
			pwd_file_to_list.append(i) 
		for i in pwd_file_to_list:
			bytes_pwd_list.append(bytes(i, 'utf-8'))
		file_to_encrypt = b''.join(bytes_pwd_list)
		encrypted_passwords = encryption_key.encrypt(file_to_encrypt)
		encrypted_pwd_file_creation(encrypted_passwords)

#ENCRYPTED PASSWORD FILE CREATION/EXPORT
def encrypted_pwd_file_creation(encrypted_passwords):
	new_file = False
	while not new_file:
		try:
			new_file = input('\nNew file name >> (Do not include \'.txt\') ')
			with open(new_file + '.txt', 'wb') as enc: 
				enc.write(encrypted_passwords)
				enc.close()
				print('\nFile has been exported.\n')
				return_to_menu.back_to_menu()
		except ValueError:
			print('Check your spelling')
			new_file = False
		

	

			
