total = int(input())


def niceness(letter, allstring):
    print("letter, allstring", letter, allstring)
    if len(allstring) == 0:
        print(0)
    else:
        allstring.append(letter)
        allstring.sort()
        try:
            print(allstring.index(letter))
        except ValueError:
            print(0)


lst = []
for i in range(total):
    lst.append(input())

for i in range(total):
    niceness(lst[i], lst[0:i + 1])
