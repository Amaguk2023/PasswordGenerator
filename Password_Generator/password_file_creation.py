import return_to_menu


# PASSWORD FILE CREATION
def pwd_file_creation(pwd_lst):
    with open('Password_List.txt', 'w') as pl:
        pl.write('\n'.join(pwd_lst))
        pl.close()
        print('\nPassword_List.txt has been exported.\n')
        return_to_menu.back_to_menu()
