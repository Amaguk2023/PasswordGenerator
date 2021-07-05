from password_list_file_creation import pwd_lst_creation

#PASSWORD CHARACTERISTIC PROMPT
def pwd_char_prompt():
	try:
		password_amount = int(input('\nAmount of passwords > '))
		password_length = int(input('\nLength of passwords > '))
		include_punctuation = False
		while not include_punctuation:
			include_punctuation = input('\nDo you want your password to include punctuation characters? (Y/n) ').lower() 
			if include_punctuation == 'y':
				pwd_lst_creation(password_amount, password_length, include_punctuation=True)			
			elif include_punctuation == 'n':
				pwd_lst_creation(password_amount, password_length, include_punctuation=False)			
			else:
				print('\nPlease check your spelling, value not accepted.')
				include_punctuation = False
	except ValueError: 
		print('\nPlease enter a valid number.')
		pwd_char_prompt()