# question 6

def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    return True


n = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
prime_num_list=filter(is_prime,n)
ls = list(prime_num_list)
print(ls)


# understanc how filter func is used and how for loops can be reduced





