a = input("숫자를 입력하세요 : ")

print(a)

print("life" "is" "good")

for i in range(10):
    print(i, end='hi')

print("/n")

g = open("dd.txt", 'w', encoding="UTF=8")
for i in range(1, 11):
    data = "%d번재 줄입니다.\n" % i
    g.write(data)
g.close()

g = open("dd.txt", 'r')
line = g.readline()
print(line)
g.close
