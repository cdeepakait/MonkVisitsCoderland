ip = input().strip()
word = ip.split(" ")[0]
num = int(ip.split(" ")[1])
lst = []
for i in range(len(word)):
    lst.append(word[i:])
lst.sort()
print(lst[num-1])
