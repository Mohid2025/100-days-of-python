# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# for fruit in fruits:
#     print("\n" +fruit)
#     print(fruit + " pie")

# student_scores = [78, 85, 62, 90, 55, 92, 88]
# total_exam_score = sum(student_scores)

# sum = 0
# for score in student_scores:
#     sum += score

# print("Total exam score:", total_exam_score)
# print("Total exam score (calculated using loop):", sum)

# student_scores = [78, 85, 62, 90, 55, 92, 88]

# sum = 0
# max_score = student_scores[0]

# for score in student_scores:
#     sum += score
#     if score > max_score:
#         max_score = score

# print("Total exam score:", sum)
# print("Highest exam score:", max_score)

# for number in range(1, 11):
#     if number % 2 == 0:
#         print(number)

# for number in range(1, 10, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number

# print("The sum of numbers from 1 to 100 is:", total)
    
import random

print("Password Generator")

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))    

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char
    
print("Your password is:", password)