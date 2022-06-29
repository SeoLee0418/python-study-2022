from operator import truediv


money = True
if money:
    print("택시를 탄다")
    print("flex")
else:
    print("걸어간다")

a = 1
b = 2

if a == b:
    print("true")
elif a < b:
    print("a is small")
else:
    print("false")

money = 2000
if money > 3000:
    print("Taxi")
elif money >= 2000:
    print("transportation")
else:
    print("walking")

pocket = ['paper', 'money', 'mobilephone']
if 'money' in pocket:
    pass
else:
    print('card')
