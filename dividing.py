def algev(x, y):
    if(x % y == 0):
        return y;
    algev(y, x % y)

def nod(x, y):
    if(x>y):
        return algev(x, y)
    return algev(y, x)

def nok(x, y):
    return x*y//nod(x, y)

x = int(input())
y = int(input())
print(nod(x, y))
print(nok(x, y))
