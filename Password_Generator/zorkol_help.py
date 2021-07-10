import return_to_menu
import sys
from art import tprint

#ENCRYPTION INFORMATION
def zorkol_help_text():
	try:
		tprint('\nZH', font='isometric1')
		print('Zorkol Help'.center(30))
		print('''
CTRL + C -> Back to menu. 

ENCRYPTION INFORMATION:

- 10 PASSWORDS WITH A LENGTH OF 20 NEED 2048 BITS (Estimated time of creation: 2 seconds.) -
- 20 PASSWORDS WITH A LENGTH OF 25 NEED 5000 BITS (Estimated time of creation: 23 seconds.) -
- 25 PASSWORDS WITH A LENGTH OF 30 NEED 7050 BITS (Estimated time of creation: 1 min and 30 seconds.) -

*** THE HIGHER THE AMOUNT/LENGTH OF PASSWORDS, THE HIGHER THE BITS AND ESTIMATED TIME OF ENCRYPTION. ***
''')
	except KeyboardInterrupt:
		print('\nGoodbye!\n')
		sys.exit()

	return_to_menu.back_to_menu()
