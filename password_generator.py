import string, secrets, sys

# Zorkol Password Generator (ZPG)
# PYTHON 3.7

# Welcome Message
print('\n')
print('''
 ZPGZPGZPGZPGZPG     ZPGZPGZPGZPGZPG        ZPGZPGZPGZPGZPG
             ZPG   ZPG             ZPG   ZPG               ZPG
            ZPG    ZPG             ZPG   ZPG               ZPG
           ZPG     ZPG             ZPG   ZPG               ZPG
          ZPG      ZPG             ZPG   ZPG               ZPG
         ZPG       ZPG             ZPG   ZPG
        ZPG        ZPG             ZPG   ZPG
       ZPG         ZPGZPGZPGZPGZPGZPG    ZPGZPGZPGZPGZPGZPGZPG
      ZPG          ZPG                   ZPG               ZPG
     ZPG           ZPG                   ZPG               ZPG
    ZPG            ZPG                   ZPG               ZPG
   ZPG             ZPG                   ZPG               ZPG
  ZPG              ZPG                   ZPG               ZPG
 ZPG               ZPG                   ZPG               ZPG
 ZPGZPGZPGZPGZPG   ZPG                      ZPGZPGZPGZPGZPG
\n''')

print('Welcome to Zorkol Password Generator (ZPG).\n')
               

def zorkol_password_generator(): #Main Function

	request = False #Variable is to False
	while not request: #Its on hold at the moment.
		
		try:

			request = input('Would you like to create a new password? (Y/n) ').lower() 
			if (request == 'y'):

				include_punctuation = False
				while not include_punctuation:

					include_punctuation = input('\nDo you want your password to include punctuation characters? (Y/n) ').lower() 

					if include_punctuation == 'y':
						with_punctuation()
					
					elif include_punctuation == 'n':
						without_punctuation()
						
					else:
						print('\nPlease check your spelling, value not accepted.')
						include_punctuation = False

			elif (request == 'n'):
				print('\nGoodbye!\n')

			else: 
				print('\nPlease check your spelling, value not accepted.\n')
				if __name__ == '__main__': zorkol_password_generator() 

		except KeyboardInterrupt: 
			print('\nGoodbye!\n')
			sys.exit(0)
			
#PASSWORDS WITH PUNCTUATITION CHARACTERS FUNCTIONS
def with_punctuation(): 
	password_length_amount_with_punctuation()

def password_length_amount_with_punctuation(): 
	try:
		password_length = int(input('\nLength of passwords > '))
		password_amount = int(input('\nAmount of passwords > '))
		amount_lst = []
		for i in range(password_amount):
			amount_lst.append(''.join(secrets.choice(list(string.ascii_letters) + list(string.digits) + list(string.punctuation)) for i in range (password_length))) 
			return export_message(amount_lst)	
				
	
	except ValueError: 
		print('\nPlease enter a valid number.')
		with_punctuation()


#PASSWORDS WITHOUT PUNCTUATITION CHARACTERS FUNCTIONS
def without_punctuation(): #Passwords including intecgers and letters only
	password_length_amount_without_punctuation()

def password_length_amount_without_punctuation():
	try:
		password_length = int(input('\nLength of passwords > '))
		password_amount = int(input('\nAmount of passwords > '))
		amount_lst = []
		for i in range(password_amount):
			amount_lst.append(''.join(secrets.choice(list(string.ascii_letters) + list(string.digits)) for i in range (password_length))) 
			return export_message(amount_lst)
	
	except ValueError:
		print('\nPlease enter a valid number.')
		without_punctuation()

#PASSWORD FILE CREATION AND EXPORT MESSAGE
def export_message(amount_lst):
	with open('Password_List.txt', 'w') as pl:
		pl.write('\n'.join(amount_lst)) 
		pl.close()
		print('\nPassword_List.txt has been exported.') 
		print('\nThank you for using ZPG!\n') 

	
zorkol_password_generator()







