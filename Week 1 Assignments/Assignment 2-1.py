#Assignment 2-1 by Diego Suarez

print("Hello World"[8])

print("thinker"[2:5])
s = "hello"
#outputs the 2nd character in the string as 0 is the first, 1 is the 2nd
print(s[1])

s = "Sammy"
#outputs every character beginning from the 3rd and onwards
print(s[2:])

mississippi_set = {'M', 'i', 's', 's','i', 's', 's', 'i', 'p', 'p', 'i'}
print("".join(mississippi_set))

print("How many phrases to determine if palindrome?")
count = int(input())

answers = []

while(count > 0):
    count -= 1

    phrase = input()
    punc = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''

    for c in phrase:
        if c in punc:
            phrase = phrase.replace(c, "")

    phrase = phrase.lower()

    if phrase == phrase[::-1]:
        answers.append('Y')
    else:
        answers.append('N')

print(" ".join(answers))

