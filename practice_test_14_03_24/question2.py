# create pythagorean triplets with sides less than or equal to 30

def pythatrip(terms):
    ls = []
    for i in range(1,terms+1):
        for j in range(2,terms+1):
            for k in range(3,terms+1):
                if k**2 == j**2 + i**2:
                    ls.append((i,j,k))
                    break
    print(ls)
                       

pythatrip(15)


