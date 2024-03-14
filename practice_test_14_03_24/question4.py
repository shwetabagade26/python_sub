# implement a generator function for factorial ,generates upto given limit n

def factorial(N):
    result = 1
    for i in range(1,N+1):
        result *= i
        yield result

terms = int(input("Enter the number of terms :  "))
for k in factorial(terms):
    print(k)

