#Assignment 1-2 by Diego Suarez

print(50+50)
print(100-10)

print(30*6)
print(6^6)
print(6**6)
print(6+6+6+6+6+6)

print("Hello World")
print("Hello World:10")

#p = 800000
#r = 6
#m = 10000
#month = 1

print("Please input total balance, interest rate, and number of months:")

x = input()
y = x.split()

p = int(y[0])
r = int(y[1])
l = int(y[2])
m = 10000
total_payment = 0

while int(p) > 0:
    interest = round(p*(r/12)/100)

    if(p <= m):
        m = p
    
    newP = p - m + interest
    
    if(newP < 0):
        newP = 0

    #print(str(month) +   " balance $" + str(p) + " interest $" + str(interest) + " payment -$" + str(m) + " new balance $" + str(newP))
    #month += 1
    p = newP

    total_payment += m

average_payment = round(total_payment/l)

print("Average payment each month: ")
print(average_payment)
