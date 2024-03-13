#where the sum of the pair is even and the first element is greater than the second element

list1 = [1,2,3]
list2 = [4,5,6]
# list3 = [(list1[val],list2[val1])%2 == 0  for val in range(len(list1)) for val1 in range(list2 ) ]
list4 = [] 


for i in range(len(list1)):
    for j in range(len(list2)):
        sum1 = list1[i] + list2[j]
        if sum1 % 2 ==0:
            list4.append((list1[i],list2[j]))
print(list4)





