import string, secrets

def pwd_lst_creation(password_amount, password_length, include_punctuation): 
	
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

def password_file_creation(amount_lst):
	with open('Password_List.txt', 'w') as pl: #creates a file .txt, the 'w' means open a text for writing, if it was an 'a' it would be for append. I keep W becasue it overwrites it on my pwd.
		pl.write('\n'.join(amount_lst)) #method write a list of strings to a file at once. Each password is going by the '\n' new line.
		print('\nPassword_List.txt has been exported.') #file is saved on the pwd that the user is currently running the program.
		print('\nThank you for using ZPG!\n') 