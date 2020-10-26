s = input()
l = s.split(' ')
set = set()
for i in l:
    if set.__contains__(i):
        print("NO")
    else:
        print("YES")
    set.add(i)
