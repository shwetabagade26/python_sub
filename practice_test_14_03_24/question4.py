# implement a generator function for factorial ,generates upto given limit n

def factorial(N):
    result = 1
    for i in range(1,N+1):
        result *= i
        yield result

for k in factorial(5):
    print(k)

