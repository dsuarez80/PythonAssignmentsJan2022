#Assignment 2-2 by Diego Suarez

x = [2, "word", float(23.54)]
print(x)

y = [1, 1, [1, 2]]
print(y[2][1])

lst = ['a', 'b', 'c']
#output every item from the position at index 1 and onwards
print(lst[1:])

weekdays_dictionary = {
    "monday" : 2,
    "tuesday" : 3,
    "wednesday" : 4,
    "thursday" : 5,
    "friday" : 6
}
print(weekdays_dictionary)

D = {'k1':[1,2,3]}
#outputs the value with key 'k1' which is an array, then indexes the array at position 1 and returns said value
print(D['k1'][1])

tup = (1,[2,3])
print(tup)

mississippi_set = {'M', 'i', 's', 's','i', 's', 's', 'i', 'p', 'p', 'i'}
print("".join(mississippi_set))

mississippi_set.add('X')
print("".join(mississippi_set))

print(set([1,1,2,3]))

for n in range(2000, 3201):
    if n % 7 == 0:
        if n % 5 != 0:
            print(n, end = ", ")

print("\nPlease input number to be calculated for factorial: ")
x = int(input())
factorial = 1

for n in range(1, x+1):
    factorial *= n

print(factorial)

powers_dictionary = {}

print("Please input number for dictionary of powers: ")
z = int(input())

for n in range(1, z+1):
    powers_dictionary[n] = n*n

print(powers_dictionary)

print("Please enter sequence of numbers separated by commas: ")
nums = input()

toList = nums.split(",")
toTuple = tuple(nums.split(","))

print(toList)
print(toTuple)

class UpperCaserBot:
    def __init__(self):
        self.string = ""

    def getString(self):
        print("Please input a string to be capitalized: ")
        self.string = input()

    def printString(self):
        print(self.string.upper())


uppercaserBot = UpperCaserBot()
uppercaserBot.getString()
uppercaserBot.printString()

