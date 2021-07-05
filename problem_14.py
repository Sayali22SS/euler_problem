l = [[i, i, 1] for i in range(1,1000000)]
def collatz(li):
    for el in li:
        if el[1] == 1:
            li.remove(el)
        elif el[1] % 2 == 0:
            el[1] = el[1] / 2
            el[2] += 1
        elif el[1] % 2 == 1:
            el[1] = 3*el[1] + 1
            el[2] += 1
    return li
while len(collatz(l)) >= 2:
l = collatz(l)

print l