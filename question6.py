# question 6

new_list = []
def is_prime(n):
    for i in range(3,len(n),2) :
        for j in range(3,n[-1]+1):
            if n[i]% j != 0 and n[i]!=j :
                new_list.append(n[i])
    print(new_list)

n = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
is_prime(n)








