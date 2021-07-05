def euler_12(num):
    i = 0
    for n in range(1,num):
        list= []
        for j in range(1, n**2):
            if (n+i) % j == 0:
                list.append(j)
                if len(list) == 500:
                    print(n+i)
                    break
        i = i + n