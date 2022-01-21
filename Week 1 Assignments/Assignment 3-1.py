#Assignment 3-1 by Diego Suarez

#numbers between 1500 and 2700 divisible by both 7 and 5
for n in range(1500, 2701):
    if n % 7 == 0:
        if n % 5 == 0:
            print(n, end = ", ")
print()

#temperature converter
while True:
    temp = input("Please input the temperature to convert, including the convention such as 45F or 60C: ")
    degree = int(temp[:-1])
    convention = temp[-1]

    if convention.upper() == "F":
        converted = round((degree - 32) * 5 / 9)
        print(temp + " is " + str(converted) + "C")
        break
    elif convention.upper() == "C":
        converted = round((9 * degree) / 5 + 32)
        print(temp + " is " + str(converted) + "F")
        break
    else:
        print("Improper convention. Try again.")

#guess a random number
import random
r = random.choice([*range(1, 10)])
print("Please guess a number between 1 and 9: ")

while(True):
    guess = int(input())
    if guess == r:
        print("Well guessed!")
        break
    else:
        print("Try again.")


#pattern printout
for x in range(5):
    for y in range(x):
        print('* ', end = "")
    print()

for x in range(5, 0, -1):
    for y in range(x):
        print('* ', end = "")
    print()

#word reverser
word = input("Please input a word to be reversed: ")
print(word[::-1])

#odd and even count
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
evens = 0
odds = 0

for x in numbers:
    if x % 2 == 0:
        evens += 1
    else:
        odds += 1

print(numbers)
print("Number of even numbers: " + str(evens))
print("Number of odd numbers: " + str(odds))

#types printout
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for x in datalist:
    print(str(x) + " is a type of " + str(type(x)))

#ignore 3 and 6
for x in range(7):
    if x == 3 or x == 6:
        continue
    print(x, end = " ")