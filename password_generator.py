#Password Generator

#ASCII CODE is a code that represents english characters as number, for example capital Z has the ASCII code 90 and the / has the ASCII code 47.



# Function

def main():

	# Random Module
	import random
	import time # This module makes inputs print slower, makes it more realistic. 

#password list

	password_list =['r8Rn#%n=8K5@=&PI286ja0N', 'w=12BrrH1$S849?e%&Ju=4G', 'KiL@ir&l64@q7T%30U3S%>7', '?0XGnqs2#s>N9%Ne?&012E4', '#1%8D9rk2jLD9l>>l>RV99&', '?TQ9L=%h89%3hzn4@9#HK5w', 'NkN85Xn=0<#c7n>P$2c7B0&', '<g%U7?95o6s37gR#SLG6?%v', '93hh<IyH6%<Qp15%&<3A0eY', '1NRLjW18O#70%>yr>>7%j8m', 'tM#G664m47@>3t#V>vOQt&6', 'R1fJh6Rb2af<101O1?##=&G', '>34a=F1D?&$ar9mG%m3A71P', 'z7t?5%>DUG4=2zwH$8&A17k', 'x=$p%#<AWJ22A6p25Xm89<z', 'KQ?5@z1mJ<mrQ51#rQ74&#6', 'KQ?5@z1mJ<mrQ51#rQ74&#6', 'n>h26M2Mu94&$8A9u@$xN<I'] # I want to add all the passwords generated and make sure that non are duplicated. This list should connect with PostgreSQL to maintain a database of all the given password lists and verify if they exist or not. HALF OF THIS HAS BEEN ACHIEVED.

#Newer version must add the generated passwords to the list.

# Random generator of ASCII characters.

	character_0 = chr(random.randint(35, 38))
	uppercase_1 = chr(random.randint(65, 90))
	uppercase_2 = chr(random.randint(65, 90))
	character_1 = chr(random.randint(60, 64))
	lowercase_1 = chr(random.randint(97, 122))
	number_1 = chr(random.randint(48, 57))
	uppercase_3 = chr(random.randint(65, 90))
	character_2 = chr(random.randint(35, 38))
	number_2 = chr(random.randint(48, 57))
	lowercase_2 = chr(random.randint(97, 122))
	character_3 = chr(random.randint(60, 64))
	number_3 = chr(random.randint(48, 57))
	lowercase_3 = chr(random.randint(97, 122))
	uppercase_4 = chr(random.randint(65, 90))
	number_4 = chr(random.randint(48, 57))
	character_4 = chr(random.randint(35, 38))
	character_5 = chr(random.randint(60, 64))
	uppercase_5 = chr(random.randint(65, 90))
	number_5 = chr(random.randint(48, 57))
	number_6 = chr(random.randint(48, 57))
	lowercase_4 = chr(random.randint(97, 122))

# Concatenation of all characters

	password = (character_0 + uppercase_1 + uppercase_2 + character_1 + lowercase_1 + str(number_1) + uppercase_3 + character_2 + str(number_2) + lowercase_2 + character_3 + str(number_3) + lowercase_3 + str(number_3) + lowercase_3 + uppercase_4 + str(number_4) + character_4 + character_5 + str(number_5) + str(number_6) + uppercase_5 + lowercase_4) 

	#print('')
	#print('Welcome to EM Password Generator!')
	#print('Our passwords are 21 characters long. They all have a mix of lowercase letters, uppercase letters, numbers and characters.')

	password_creation = False #Set to false so the while loop activates after gets an input and becomes true.
	

	# Beginning of the while loop. #and recreate_password == True:


	while password_creation == False:	 	
		print('')
		password_creation = raw_input('''Please write 'generate' to receive your new password > ''') #Status changed from false to true.
	
		if password_creation == 'generate' or password_creation == 'Generate':
			print('')
			print('Generating password...')
			p_list = list(password) # Create a list with the randomly generated word.
			random.shuffle(p_list) # Shuffle that list of words.
			p_list_string = ''.join([str(letter) for letter in p_list]) #String is joined using list comprehension.
			print('')
			time.sleep(3)
			print('Verifying password doesn\'t exist...')
			print('')	

		
			if (p_list_string not in password_list):
				time.sleep(3)
				print('Process complete, here\'s your password: ' + p_list_string) # Print the final string.
				print('')
				recreate_password = raw_input('Thank you for using our service! Would you like to create another password? ')


				if recreate_password == 'yes':
					main()
			
				else:
					print('')
					print('Goodbye!')
					print('')
					break
				
		
			elif (p_list_string in password_list): # verifies that the password is not included in the password_list.
				new_list = list(password)
				random.shuffle(new_list)
				new_password_1 = ''.join([str(new_list) for letter in new_list]) #String is joined using list comprehension.			
			

				if (new_password_1 not in password_list): 
					time.sleep(3)
					print('Process complete, here\'s your password: ' + new_password_1) # Print the final string.
					print('')
					recreate_password = raw_input('Thank you for using our service! Would you like to create another password? ')

					
					if recreate_password == 'yes': #Back to the beginning
						main()
					else:
						print('')
					 	print('Goodbye!')
						print('')
						break
			

				elif (new_password_1 in password_list):	# 2nd verification to check new password is not included in the password_list.
					new_list_2 = list(password)
					random.shuffle(new_list_2)
					new_password_2 = ''.join([str(letter) for letter in new_list_2])
				
				
					if (new_password_2 not in password_list):
						time.sleep(3)
						print('Process complete, here\'s your password: ' + new_password_2) # Print the final string.
						print('')
						recreate_password = raw_input('Thank you for using our service! Would you like to create another password? ')

						
						if recreate_password == 'yes': #Back to the beginning
							main()
						
						else:
							print('')
					 		print('Goodbye!')
							print('')
							break	


					elif (new_password_2 in password_list): # 3rd verification to check new password is not included in the password_list.
							new_list_3 = list(password)
							random.shuffle(new_list_3)
							new_password_3 = ''.join([str(letter) for letter in new_list_3])
						
		
							if (new_password_3 not in password_list): 	
								time.sleep(3)
								print('Process complete, here\'s your password: ' + new_password_2) # Print the final string.
								print('')
								recreate_password = raw_input('Thank you for using our service! Would you like to create another password? ')	
								
								if recreate_password == 'yes':#Back to the beginning
									main()
					
								else:
									print('')
					 				print('Goodbye!')
									print('')
									break	

		
							elif (new_password_3 in password_list): # 4th verification to check new password is not included in the password_list.
								new_list_4 = list(password)
								random.shuffle(new_list_4)
								new_password_4 = ''.join([str(letter) for letter in new_list_4])


								if (new_password_4 not in password_list):
									time.sleep(3)
									print('Process complete, here\'s your password: ' + new_password_4) # Print the final string.
									print('')
									recreate_password = raw_input('Thank you for using our service! Would you like to create another password? ')
									
									if recreate_password == 'yes': #Back to the beginning
										main()	
			
									else:
										print('')
					 					print('Goodbye!')
										print('')
										break	

							
								elif (new_password_4 in password_list): # 5th and last verification to check new password is not included in the password_list.
									new_list_5 = list(password)
									random.shuffle(new_list_4)
									new_password_5 = ''.join([str(letter) for letter in new_list_5])
									time.sleep(3)
									print('Process complete, here\'s your password: ' + new_password_5) # Print the final string.
									print('')
									recreate_password = raw_input('Thank you for using our service! Would you like to create another password? ')

									
									if recreate_password == 'yes': #Back to the beginning
										main()	

									else:
										print('')
					 					print('Goodbye!')
										print('')
										break	


		else:
			print('')
			print('ERROR 2023: Answer not valid answer. Please check your spelling.')
			print('')
			main()
			
				
# This has been taken out of the main function so when they respond 'yes' to get a new password it doesn't print the welcome again. ACHIEVED

print('')
print('Welcome to EM Password Generator!')
print('Our passwords are 21 characters long. They all have a mix of lowercase letters, uppercase letters, numbers and characters.')

main() # Function Call.
							
							

		
		

