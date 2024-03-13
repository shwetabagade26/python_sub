# zip two lists together and create a list of tuples where each tuple contains coressponding elements

list1 = [1,2,3]
list2 = ['a','b','c']
result= []
result2 = list(zip(list1,list2))
print("Using zip func",result2)

def zipping(list1, list2):
    for i in range(len(list1)):
        tup = (list1[i],list2[i])
        result.append(tup)
    print(result)

zipping(list1,list2)

# output [(1, 'a'), (2, 'b'), (3, 'c')]