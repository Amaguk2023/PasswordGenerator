import password_generator
import sys
import art
import return_to_menu


# PASSWORD CREATION PROMPT
def pwd_creation_prompt():
    art.tprint('\nZPG', font='isometric1')
    print('Zorkol Password Generator'.center(43))
    password_amount = False
    password_length = False
    while not password_amount and not password_length:
        try:
            password_amount = int(input('\nAmount of passwords > '))
            password_length = int(input('\nLength of passwords > '))
            include_punctuation = False
            while not include_punctuation:
                include_punctuation = input(
                    '\nDo you want your password to include punctuation characters? (Y/n) ').lower()
                if include_punctuation == 'y':
                    password_generator.pwd_lst_generator(password_amount, password_length, include_punctuation=True)
                elif include_punctuation == 'n':
                    password_generator.pwd_lst_generator(password_amount, password_length, include_punctuation=False)
                else:
                    print('\nPlease check your spelling, value not accepted.')
                    include_punctuation = False
        except ValueError:
            print('\nPlease check your spelling, value not accepted.')
            password_amount = False
            password_length = False
        except KeyboardInterrupt:
            print('\n')
            return_to_menu.back_to_menu()
