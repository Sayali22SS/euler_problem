def largest_product_series(n, series):
    series = str(series)
    largest = 0
    for i in range(0,1000-n):
         temp = np.prod([int(series[j]) for j in range(i,n+i)])
         largest = max(temp, largest)
    return largest