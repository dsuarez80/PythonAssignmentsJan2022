#Assignment 4-1 by Diego Suarez

def func():
    print("Hello World")

func()

def func1(name):
    print("Hi my name is", name)

func1("Diego")

def func3(x, y, z):
    if z:
        return x
    return y

print(func3("hello", "goodbye", True))
print(func3("hello", "goodbye", False))

def func4(x, y):
    return x + y

print(func4(5, 7))

def is_even(x):
    if x % 2 == 0:
        return True
    return False

print(is_even(5))
print(is_even(4))

def is_greater(x, y):
    if x <= y:
        return False
    return True

print(is_greater(10, 5))
print(is_greater(4, 8))

def sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(sum(5, 6, 7, 8, 9))

def string_caser(s):
    l = []
    for i, c in enumerate(s):
        if i % 2 == 0:
            l.append(c.upper())
        else:
            l.append(c.lower())
    return ''.join(l)


print(string_caser("this is my string"))

def lesser_greater(x, y):
    if x % 2 == 0 and y % 2 == 0:
        if x > y:
            return y
    else:
        if x > y:
            return x
    return x

print(lesser_greater(4, 6))
print(lesser_greater(7, 6))
print(lesser_greater(2, 2))

def start_with_same(s1, s2):
    if s1[0].upper() == s2[0].upper():
        return True
    return False

print(start_with_same("Hello", "yellow"))
print(start_with_same("Hello", "hollow"))

def get_square(x):
    return x ** 2

print(get_square(24))

def cap_first_fourth(s):
    l = []
    for i, c in enumerate(s):
        if i == 0 or i == 3:
            l.append(c.upper())
        else:
            l.append(c.lower())
    return ''.join(l)

print(cap_first_fourth("word"))