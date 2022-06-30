from curses import termattrs


treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("Hit the tree : %d" % treehit)
    if treehit == 10:
        print("treehit is done")


coffee = 10
money = 300
while money:
    print("get some coffee")
    coffee = coffee - 1
    print("coffee is left %d." % coffee)
    if not coffee:
        print("No coffee")
        break

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)
