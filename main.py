import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the pypassword Generator!!")
answer=[]
nr_letters = int(input("How many letters would you like in your password?"))
nr_sym = int(input("How many symbols would you like?"))
nr_num = int(input("How many numbers would you like?"))

for i in range(0 , nr_letters-nr_num-nr_sym):
    answer.append(random.choice(letters))

for i in range(0 , nr_sym):
    answer.append(random.choice(symbols))

for i in range(0 , nr_num):
    answer.append(random.choice(numbers))
print("EASY LEVEL:")
a = ""
for i in answer:
   a += i
print(a)

print("HARD LEVEL")

random.shuffle(answer)
ans = ""
for i in answer:
    ans += i

print(ans)
