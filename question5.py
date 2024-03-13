# prime numbers up to 20
def is_prime(num):
    list1 = [2]
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            break
    else:
        # print(num)
        list1.append(num)
        

for k in range(3,100):
    is_prime(k)
