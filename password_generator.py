import string, secrets, sys

# Zorkol Password Generator (ZPG)
# PYTHON 3.7

#WELCOME MESSAGE
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
               

#PASSWORD CREATION PROMPT
def create_password_prompt():
	try:
		
		request = False 
		while not request: 
		
			request = input('Would you like to create a new password? (Y/n) ').lower()

			if (request == 'y'):
				password_characteristic_prompt()
				
			elif (request == 'n'):
				print('\nGoodbye!\n')

			else: 
				print('\nPlease check your spelling, value not accepted.\n')
				request = False 

	except KeyboardInterrupt: 
		print('\nGoodbye!\n')
		sys.exit()


#PASSWORD AMOUNT, LENGH OF PASSWORD AND INCLUDE/EXCLUDE PUNCTUATION CHARACTERS PROMPT
def password_characteristic_prompt():

	try:
		
		password_amount = int(input('\nAmount of passwords > '))
		password_length = int(input('\nLength of passwords > '))
		
		include_punctuation = False
		while not include_punctuation:

			include_punctuation = input('\nDo you want your password to include punctuation characters? (Y/n) ').lower() 
			
			if include_punctuation == 'y':
				password_list_creation(password_amount, password_length, include_punctuation = True)
					
			elif include_punctuation == 'n':
				password_list_creation(password_amount, password_length, include_punctuation = False)
						
			else:
				print('\nPlease check your spelling, value not accepted.')
				include_punctuation = False

	except ValueError: 
		print('\nPlease enter a valid number.')
		password_characteristic_prompt()
			

#PASSWORD LIST CREATION 
def password_list_creation(password_amount, password_length, include_punctuation): 
	
	if include_punctuation == True:
		amount_lst = []
		for i in range(password_amount):
			amount_lst.append(''.join(secrets.choice(list(string.ascii_letters) + list(string.digits) + list(string.punctuation)) for i in range (password_length)))
			if len(amount_lst) == password_amount:
				password_file_creation(amount_lst)

	else:
		amount_lst = []
		for i in range(password_amount):
			
			amount_lst.append(''.join(secrets.choice(list(string.ascii_letters) + list(string.digits)) for i in range (password_length)))
			if len(amount_lst) == password_amount:
				password_file_creation(amount_lst)


#PASSWORD FILE CREATION AND FINAL MESSAGE
def password_file_creation(amount_lst):
	with open('Password_List.txt', 'w') as pl: 
		pl.write('\n'.join(amount_lst)) 
		print('\nPassword_List.txt has been exported.') 
		print('\nThank you for using ZPG!\n') 

	

if __name__ == '__main__': 
	create_password_prompt() 

