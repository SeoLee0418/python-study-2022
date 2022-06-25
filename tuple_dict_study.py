a = (1, 2, 3, 4)
b = (5, 6)
# del[0:1] --> 튜플은 값 변경 불가.

print(a[2])
print(a[0:3])
print(a + b)
print(a * 3)

## dic = {'name': 'Seoyong', 'age': 30}
# print(dic['name'])

a = {1: 'a'}
a['name'] = '서용'
del a[1]

print(a)

# 주의사항  -- a = {1 : 3, 1 : 4}키워드가 같으면 안됨

a = {1: 3, 2: 4, 3: 5}
print(a.keys())
print(a.values())
print(a.items())

# a.clear()
# print(a)

print(a.get(4, "nothing"))
