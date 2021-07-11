import password_creation_prompt
from decryption import pwd_decryption
from art import tprint
import private_public_keys_creation
import encryption
import sys
import zorkol_help


# MENU PROMPT
def initial_prompt():
    tprint('\nMENU', font='isometric1')
    print('''\nZorkol Password Generator (ZPG)
Zorkol Key Generator (ZKG)
Zorkol Password Encryptor (ZPE)
Zorkol Password Decryptor (ZPD)
Zorkol Help (ZH)
Exit''')
    menu = False
    while not menu:

        menu = input('\n>> ').lower()
        if menu == 'zpg':
            password_creation_prompt.pwd_creation_prompt()
        elif menu == 'zkg':
            private_public_keys_creation.new_pr_key_pu_key_creation()
        elif menu == 'zpe':
            encryption.pwd_encryption()
        elif menu == 'zpd':
            pwd_decryption()
        elif menu == 'zh':
            zorkol_help.zorkol_help_text()
        elif menu == 'exit':
            sys.exit()
        else:
            print('\nPlease check your spelling, value not accepted.')
            menu = False


if __name__ == '__main__':
    initial_prompt()
