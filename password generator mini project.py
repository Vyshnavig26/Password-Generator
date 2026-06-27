import random
import string
lowercase=string.ascii_lowercase
uppercase=string.ascii_uppercase
digits=string.digits
punctuation=string.punctuation
print('WELCOME TO PASSWORD GENERATOR')
n_lowercase=int(input('How many lowercase letters you want in your password\n'))
n_uppercase=int(input('How many uppercase letters you want in your password\n'))
n_digits=int(input('How many digits you want in your password\n'))
n_punctuation=int(input('How many punctuations you want in your password\n'))
password_list=[]
for i in range(1,n_lowercase+1):
    char=random.choice(lowercase)
    password_list+=char
for i in range(1,n_uppercase+1):
    char=random.choice(uppercase)
    password_list+=char
for i in range(1,n_digits+1):
    char=random.choice(digits)
    password_list+=char
for i in range(1,n_punctuation+1):
    char=random.choice(punctuation)
    password_list+=char
random.shuffle(password_list)
password=''
for char in password_list:
    password+=char
print(password)