end = False
all = list(range(2, 2000000))
delnum = 2
while all.index(delnum)+1 <= len(all) and end == False:
    for x in all:
        if x % delnum == 0 and delnum != x:
            all.remove(x)
    if all.index(delnum)+1 == len(all):
        end = True
    if all.index(delnum)+1 <= len(all) and end == False:
        delnum = all[all.index(delnum) + 1]
print(sum(all))
