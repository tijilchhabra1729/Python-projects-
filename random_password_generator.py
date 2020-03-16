import random


num_alpha = input("Enter the number of alphabets you want in the password:  ")
num_numbers = input("Enter the number of numbers you want in the password:  ")
num_spechar = input("Enter the number of special characters you want in the password:  ")

alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spechar_list = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '<', '>', ',', '.', '?']
i = 1
j = 1
k = 1
password = []
final_password = ''

if int(num_alpha) + int(num_numbers) + int(num_spechar) < 6:
    print("Password should contain minimum of 6 characters.")

while i <= int(num_alpha):
    ran_alpha = random.randint(0, 26)
    a = alpha_list[ran_alpha]
    password.append(a)
    i += 1

while j <= int(num_numbers):
    ran_num = random.randint(0, 9)
    b = num_list[ran_num]
    password.append(b)
    j += 1

while k <= int(num_spechar):
    ran_spechar = random.randint(0, 15)
    c = spechar_list[ran_spechar]
    password.append(c)
    k += 1

random.shuffle(password)
legnth_password = len(password)

for l in password:
    final_password += l

print("Your random password is:  " + final_password)