test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)


a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first)
    print(last)


marks = [90, 25, 67, 45, 80]
number = 0
for Mark in marks:
    number = number + 1
    if Mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)

# 구구단
for i in range(1, 10):
    for k in range(1, 10):
        print(i*k, end=" ")
    print(' ')

b = [1, 2, 3, 4]
result = [num * 3 for num in b]
print(result)
