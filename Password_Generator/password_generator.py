import secrets
import string
import password_file_creation


# PASSWORD LIST CREATION
def pwd_lst_generator(password_amount, password_length, include_punctuation):
    pwd_lst = []
    for _ in range(password_amount):
        if include_punctuation:
            pwd_lst.append(''.join(
                secrets.choice(list(string.ascii_letters) + list(string.digits) + list(string.punctuation)) for i in
                range(password_length)))
        else:
            pwd_lst.append(''.join(
                secrets.choice(list(string.ascii_letters) + list(string.digits)) for i in range(password_length)))
        if len(pwd_lst) == password_amount:
            password_file_creation.pwd_file_creation(pwd_lst)
