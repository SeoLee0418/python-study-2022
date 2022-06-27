# 집합
# 선언
s1 = set([1, 2, 3])
print(s1)

# 중복과 순서가 없다
s2 = set("hello")
print(s2)

# 활용
ab = [1, 2, 3, 4, 3, 2]
bc = list(set(ab))
print(bc)

# 교집합
s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9])
print(s3 & s4)
print(s3.intersection(s4))

# 합집합
print(s3 | s4)
print(s3.union(s4))

# 차집합
print(s3 - s4)
print(s3. difference(s4))

# 갑 추가하기
s1.add(4)
print(s1)

# 여러개 추가하기
s1.update([5, 6, 7])
print(s1)

# 특정값 지우기
s1.remove(4)
print(s1)

# bool
# 선언
a = True

# 활용
if a:
    print("hello")

b = [1, 2, 3, 4]

while b:
    b.pop()
    print(b)
