# prime numbers up to 20
# prime = [x for x in range(2, 100) if all(x % y != 0 for y in range(2, x))]

# def is_prime(num):
#     for i in range(2,num+1):
#         for j in range(2,i):
#                 if i%j != 0 :
#                     yield i


# def is_even(num):
#      for i in range(2,num+1):
#           if i%2 == 0:
#                yield i

# # for i in is_even(20):
#     #  print(i)

# for k in is_prime1(20):
#     print(k)

def prime_nums(terms):
    flag=True
    for num in range(2,terms):
        flag=True
        for i in range(2,num):
            if(num%i == 0):
                flag = False
        if flag:
            yield num

for number in prime_nums(20):
    print(number)    


# need to understand generator func properly