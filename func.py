from unittest import result


def sum(a, b):
    result = a+b
    return result


print(sum(2, 3))

mylist = [1, 2, 3]
print(mylist.pop())
mylist.append(4)
print(mylist)


def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


print(sum_many(1, 2, 3))


def sum_and_mul(a, b):
    return a+b, a*b


print(sum_and_mul(3, 4))  # 튜플s


def myself(name, age, man=True):
    print("My name is %s" % name)
    print("I'm %d old" % age)
    if man:
        print("Man")
    else:
        print("Lady")


print(myself("Seoyong", 30, True))


def add(a, b): return a+b


a = add(3, 4)
print(a)


c = input("press the number : ")
d = input("press the number : ")
