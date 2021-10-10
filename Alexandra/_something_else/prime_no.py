def prim(n):
    nrp = 0
    for i in range(2, int(n ** 1 / 2) + 1):
        if n % i == 0:
            nrp += 1

    if nrp == 0:
        return True
    else:
        return False


x = 0
nr = 2
while x < 5:
    if prim(nr):
        x += 1
        print(nr)
    nr += 1

