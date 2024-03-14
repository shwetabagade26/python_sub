#where the sum of the pair is even and the first element is greater than the second element

list1 = [1,2,3]
list2 = [4,5,6]
# list3 = [ (list1[i],list2[j])for i in range(len(list1) for j in range(list2) if (list1[i] + list2[j]) % 2 == 0 )]
list3 = [(x, y) for x in list1 for y in list2 if (x + y) % 2 == 0]
print(list3)
list4 = [] 


for i in range(len(list1)):
    for j in range(len(list2)):
        sum1 = list1[i] + list2[j]
        if sum1 % 2 ==0:
            list4.append((list1[i],list2[j]))
print(list4)





