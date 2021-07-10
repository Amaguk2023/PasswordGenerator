import sys
from Crypto.PublicKey import RSA
import menu_prompt
from art import tprint 
import return_to_menu

#PRIVATE AND PUBLIC KEY CREATION
def new_pr_key_pu_key_creation():
	tprint('''\nZKG\n''', font='isometric1')
	print('''            Zorkol Key Generator''')
	bits = False
	while not bits:
		try:
			bits = int(input('\nAmount of bits >> '))
			private_key_generation = RSA.generate(bits) #Generating private key (RsaKey object) of key length of 2048 bits
			public_key_generation = private_key_generation.public_key() #Generating the public key (RsaKey object) from the private key
			final_private_key = private_key_generation.export_key().decode()
			final_public_key = public_key_generation.export_key().decode()
			new_pr_key_pu_key_export(final_private_key, final_public_key)
		except ValueError:
			print('''\nPossible errors:
Bits are not enough for encryption.
Value inserted is not accepted.\n''')
			bits = False
		except KeyboardInterrupt:
			print('\n')
			return_to_menu.back_to_menu()

#PRIVATE AND PUBLIC KEY FILE CREATION/EXPORT
def new_pr_key_pu_key_export(final_private_key, final_public_key):
	with open('private_key.pem', 'w') as pr:
		pr.write(final_private_key)
		pr.close()
		with open('public_key.pem', 'w') as pu:
			pu.write(final_public_key)
			pu.close()	
			print('\nPrivate and public keys have been exported.\n')
			return_to_menu.back_to_menu()


