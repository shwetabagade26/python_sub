# prime numbers up to 20
def is_prime(num):
    list1 = [2]
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            break
    else:
        # print(num)
        yield num
        

for k in is_prime(100):
    print(k)
    
