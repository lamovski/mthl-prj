l = []
while True:
    n = int(input())
    if n == 0:
        break
    l.append(n)
s=set(l)

print(len(s))
