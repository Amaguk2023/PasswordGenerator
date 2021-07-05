import sys
from art import *
import password_characteristic_prompt

# PYTHON 3.7

#WELCOME MESSAGE
tprint('''\nZPG''', font='isometric1')

print('Welcome to Zorkol Password Generator (ZPG).\n')
               
#PASSWORD CREATION PROMPT
def create_password_prompt():
	try:
		
		request = False 
		while not request: 
		
			request = input('Would you like to create a new password? (Y/n) ').lower() 

			if (request == 'y'):
				password_characteristic_prompt.pwd_char_prompt() 
				
			elif (request == 'n'):
				print('\nGoodbye!\n')

			else: 
				print('\nPlease check your spelling, value not accepted.\n')
				request = False 

	except KeyboardInterrupt: 
		print('\nGoodbye!\n')
		sys.exit()
	

if __name__ == '__main__': 
	create_password_prompt()





















