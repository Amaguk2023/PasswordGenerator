from password_list_file_creation import pwd_lst_creation

def pwd_char_prompt():

	try:

		password_amount = int(input('\nAmount of passwords > '))
		password_length = int(input('\nLength of passwords > '))
		
		include_punctuation = False
		while not include_punctuation:

			include_punctuation = input('\nDo you want your password to include punctuation characters? (Y/n) ').lower() #This sets the variable to False and the program begins.
			
			if include_punctuation == 'y':
				pwd_lst_creation(password_amount, password_length, include_punctuation = True)
					
			elif include_punctuation == 'n':
				pwd_lst_creation(password_amount, password_length, include_punctuation = False)
						
			else:
				print('\nPlease check your spelling, value not accepted.')
				include_punctuation = False

	except ValueError: #ignores error and jumps to the next print statement + runs back to the functtion.
		print('\nPlease enter a valid number.')
		pwd_char_prompt()