def sum_square_diff(n):
    num = range(1, n+1)
    sum_sq= sum(i**2 for i in num)
    sq_sum = sum(num)**2
    return sq_sum - sum_sq

print(sum_square_diff(100))