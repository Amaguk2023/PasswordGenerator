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

	request = False 
	while not request: 
		
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
			sys.exit()
			

#PASSWORDS WITH PUNCTUATITION CHARACTERS FUNCTIONS
def with_punctuation(): 
	password_length_amount_with_punctuation()

def password_length_amount_with_punctuation(): 
	try:
		amount_lst = []
		password_amount = int(input('\nAmount of passwords > '))
		password_length = int(input('\nLength of passwords > '))
		for i in range(password_amount):
			amount_lst.append(''.join(secrets.choice(list(string.ascii_letters) + list(string.digits) + list(string.punctuation)) for i in range (password_length)))  
			if len(amount_lst) == password_amount:
				password_list_creation(amount_lst) 

	except ValueError: 
		print('\nPlease enter a valid number.')
		with_punctuation()


#PASSWORDS WITHOUT PUNCTUATITION CHARACTERS FUNCTIONS
def without_punctuation(): 
	password_length_amount_without_punctuation()

def password_length_amount_without_punctuation():
	try:
		amount_lst = []
		password_length = int(input('\nLength of passwords > '))
		password_amount = int(input('\nAmount of passwords > '))
		for i in range(password_amount):
			
			amount_lst.append(''.join(secrets.choice(list(string.ascii_letters) + list(string.digits)) for i in range (password_length)))
			if len(amount_lst) == password_amount:
				password_list_creation(amount_lst)
	
	except ValueError:
		print('\nPlease enter a valid number.')
		without_punctuation()


#PASSWORD FILE CREATION
def password_list_creation(amount_lst):
	with open('Password_List.txt', 'w') as pl: 
		pl.write('\n'.join(amount_lst)) 
		pl.close()
		exit_message()


#FINAL MESSAGE
def exit_message():
	print('\nPassword_List.txt has been exported.') 
	print('\nThank you for using ZPG!\n') 		
	
zorkol_password_generator()





















