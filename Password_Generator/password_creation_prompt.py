import sys
from art import *
import password_characteristic_prompt

# Zorkol Password Generator (ZPG)
# PYTHON 3.7

#WELCOME MESSAGE
tprint('''\nZPG''', font='isometric1')

print('Welcome to Zorkol Password Generator (ZPG).\n')
               
#PASSWORD CREATION PROMPT
def create_password_prompt():
	try:
		
		request = False #Variable is to False
		while not request: #Its on hold at the moment.
		
			request = input('Would you like to create a new password? (Y/n) ').lower() #This sets the variable to False and the program begins.

			if (request == 'y'):
				password_characteristic_prompt.pwd_char_prompt() #PASSWORD AMOUNT, LENGH OF PASSWORD AND INCLUDE/EXCLUDE PUNCTUATION CHARACTERS PROMPT
				
			elif (request == 'n'):
				print('\nGoodbye!\n')

			else: 
				print('\nPlease check your spelling, value not accepted.\n')
				request = False #Sets back request to False and process restarts.

	except KeyboardInterrupt: # In case CTRL + C is used, it closes the program without giving an error. 
		print('\nGoodbye!\n')
		sys.exit()
	

if __name__ == '__main__': 
	create_password_prompt()





















