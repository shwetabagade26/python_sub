# a list prime numbers between 1 to 100 using list comprehension
prime = [x for x in range(2, 100) if all(x % y != 0 for y in range(2, x))]
print(prime)