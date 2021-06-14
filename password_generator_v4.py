import time, random, string, secrets, sys

# Zorkol Password Generator (ZPG)


# PYTHON 3.7


# Welcome Message

print('')
print('')

print('                  ZPGZPGZPGZPGZPG     ZPGZPGZPGZPGZPG        ZPGZPGZPGZPGZPG')
print('                              ZPG   ZPG             ZPG   ZPG               ZPG')
print('                             ZPG    ZPG             ZPG   ZPG               ZPG')
print('                            ZPG     ZPG             ZPG   ZPG               ZPG')
print('                           ZPG      ZPG             ZPG   ZPG               ZPG')
print('                          ZPG       ZPG             ZPG   ZPG')
print('                         ZPG        ZPG             ZPG   ZPG')
print('                        ZPG         ZPGZPGZPGZPGZPGZPG    ZPGZPGZPGZPGZPGZPGZPG')
print('                       ZPG          ZPG                   ZPG               ZPG')
print('                      ZPG           ZPG                   ZPG               ZPG')
print('                     ZPG            ZPG                   ZPG               ZPG')
print('                    ZPG             ZPG                   ZPG               ZPG')
print('                   ZPG              ZPG                   ZPG               ZPG')
print('                  ZPG               ZPG                   ZPG               ZPG')
print('                  ZPGZPGZPGZPGZPG   ZPG                      ZPGZPGZPGZPGZPG')
print('')
print('')
print('''                            Welcome to Zorkol Password Generator (ZPG).''')

                  



# Function Definition

def zorkol_password_generator():

	try:
		request = input('Would you like to create a new password? (Y/N) ')
		print('')
		if request == 'y' or request == 'Y':
			print('Generating Password...')
			time.sleep(3)
			print('')
			password_list = list(string.ascii_letters) + list(string.digits)
			random.shuffle(password_list)
			password = ''.join(secrets.choice(password_list) for i in range (25))
			print('Here is your password: ' + password)
			print('')
			print('Thank you for using ZPG!')
			print('')

		elif request == 'n' or request == 'N':
			print('Goodbye!')
	
		elif request != 'Y' or request != 'y' or request != 'n' or request != 'N': 
			print('')
			print('Please check your spelling. Value not accepted.')
			print('')
			zorkol_password_generator()

	except KeyboardInterrupt: # In case CTRL + C is used, it closes the program without giving an error. 
		print(' Goodbye!')
		sys.exit() 
		
		

zorkol_password_generator()
		
		








	


