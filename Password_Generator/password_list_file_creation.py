import string, secrets

#PASSWORD LIST CREATION
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

#PASSWORD FILE CREATION AND EXPORT
def password_file_creation(amount_lst):
	with open('Password_List.txt', 'w') as pl: 
		pl.write('\n'.join(amount_lst)) 
		print('\nPassword_List.txt has been exported.') 
		print('\nThank you for using ZPG!\n') 