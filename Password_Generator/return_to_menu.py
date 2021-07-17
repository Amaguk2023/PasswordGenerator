import __main__
import sys

#RETURN TO MENU PROMPT
def back_to_menu():
	return_to_menu = False
	while not return_to_menu:
		return_to_menu = input('Return to menu or exit? (M/e)\n').lower()
		if return_to_menu == 'm':
			__main__.initial_prompt()
		elif return_to_menu == 'e':
			print('\nGoodbye!\n')
			sys.exit()

		else:
			print('\nPlease check your spelling, value not accepted.\n')
			return_to_menu = False