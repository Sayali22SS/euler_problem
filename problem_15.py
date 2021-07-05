from math import factorial
from time import time

start = time()

def nck(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k))
print 'Number of lattice paths is: '+str(nck(20+20,20))
end = time()
print end-start