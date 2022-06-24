# 1
from audioop import reverse


k = 80
e = 75
m = 55

result = (k + e + m)/3

print(result)

# 2
a = 13
if a % 2 == 1:
    print("13은 홀수입니다")
else:
    print("13은 짝수입니다")

# 3
a = "8811201068234"

print(a[:6])
print(a[6:])

# 4
pin = "881120-1068234"
gender = pin[7]
print(gender)

# 5
g = "a:b:c:d"
print(g.replace(":", "#"))

# 6
h = [1, 3, 5, 4, 2]
h.sort()
h.reverse()
print(h)

# 7
k = ['Life', 'is', 'too', 'short']
k = " ".join(['Life', 'is', 'too', 'short'])
print(k)
