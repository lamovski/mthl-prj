n = int(input())
res=0
s = set()
for i in range(0, n):
    str = input()
    s |= set(str.split(' '))
print(len(s))
