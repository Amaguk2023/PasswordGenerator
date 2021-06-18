import string
import secrets
import sys

# Zorkol Password Generator (ZPG)


# PYTHON 3.7


# Welcome Message

print('\n')
print(' ZPGZPGZPGZPGZPG     ZPGZPGZPGZPGZPG        ZPGZPGZPGZPGZPG')
print('             ZPG   ZPG             ZPG   ZPG               ZPG')
print('            ZPG    ZPG             ZPG   ZPG               ZPG')
print('           ZPG     ZPG             ZPG   ZPG               ZPG')
print('          ZPG      ZPG             ZPG   ZPG               ZPG')
print('         ZPG       ZPG             ZPG   ZPG')
print('        ZPG        ZPG             ZPG   ZPG')
print('       ZPG         ZPGZPGZPGZPGZPGZPG    ZPGZPGZPGZPGZPGZPGZPG')
print('      ZPG          ZPG                   ZPG               ZPG')
print('     ZPG           ZPG                   ZPG               ZPG')
print('    ZPG            ZPG                   ZPG               ZPG')
print('   ZPG             ZPG                   ZPG               ZPG')
print('  ZPG              ZPG                   ZPG               ZPG')
print(' ZPG               ZPG                   ZPG               ZPG')
print('ZPGZPGZPGZPGZPG    ZPG                      ZPGZPGZPGZPGZPG\n')

print('Welcome to Zorkol Password Generator (ZPG).\n')


# Function Definition


def zorkol_password_generator():

	request = False
	while request == False:

		try:

			request = input('Would you like to create a new password? (Y/N) ')
			if request.upper() in ('Y', '\n'):

				puntn = False

				while puntn == False:
					puntn = input(
					'\nDo you want your password to include punctuation characters? (Y/N) ')
					
					if puntn.upper() in 'Y':
						try:
							password_length = int(
								input('\nLength of passwords > '))
							password_amount = int(
								input('\nAmount of passwords > '))
							amount_lst = []
							if password_length == 0 or password_amount < 0:
								print("You have entered a negative number. Please try again with a positive one!")
						except Exception as error:
							print("You have given an incorrect value for either the lenght of the password or the amount of passwords to be generated.")
							print(error)
							sys.exit()

						while len(amount_lst) <= password_amount:

							amount_lst.append(''.join(secrets.choice(list(string.ascii_letters) + list(
								string.digits) + list(string.punctuation)) for i in range(password_length)))

							if len(amount_lst) == password_amount:
								with open('Password_List.txt', 'w') as pl:
									pl.writelines('\n'.join(amount_lst))
									pl.close()
									print(
										'\nPassword_List.txt has been exported.')
									print('\nThank you for using ZPG!\n')

					elif puntn.upper() in 'N':
						password_length = int(
							input('\nLength of passwords > '))
						password_amount = int(
							input('\nAmount of passwords > '))
						amount_lst = []

						while len(amount_lst) <= password_amount:

							amount_lst.append(''.join(secrets.choice(list(
								string.ascii_letters) + list(string.digits)) for i in range(password_length)))

						if len(amount_lst) == password_amount:
								with open('Password_List.txt', 'w') as pl:
									pl.writelines('\n'.join(amount_lst))
									pl.close()  # file is closed
									print(
										'\nPassword_List.txt has been exported.')
									print('\nThank you for using ZPG!\n')

					else:
						print('\nPlease check your spelling, value not accepted.')
						puntn = False

			elif request.upper() in ('N', '\n'):
				print('\nGoodbye!\n')

			else:
				print('\nPlease check your spelling, value not accepted.\n')
				request = False

		except KeyboardInterrupt:
			print('\nGoodbye!\n')
			sys.exit()


zorkol_password_generator()
