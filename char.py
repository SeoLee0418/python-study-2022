# 자료형 : 숫자 문자 bool 변수 리스트 튜플 딕셔너리 집합

# 정수형
from tokenize import Number


a = 1
print(type(a))

# 실수형
b = 3.14
print(type(a))

# 사칙연산
print(a + b)

# 문자형
c = "hello world"
print(type(c))
d = '  My favorite\' is you'
print(d)

e = "she is"
f = "hot"
print(e + f)

g = "abcdefg"
print(g[-1])
print(g[1:5:2])

number = 4
day = "four"
h = "i have %d apples. so i will sell it %s days" % (number, day)
print(h)
