# frequency of each word in the list and store result in dictionary

Input_list = ["Python is a powerful programming language",
              "Python is used for web development",
              "Python has a rich set of libraries"]


# def counter(ls):  #length of each word
#     counter_dict = {}
#     for i in range(len(ls)):
#         new_ls = ls[i].split()
#         for j in range(len(new_ls)):
#             frequency = len(new_ls[j])
#             counter_dict[new_ls[j]] = frequency
#     print(counter_dict)

def counter(ls):
    counter_dict = {}
    new_ls=str(Input_list)
    print(new_ls)
    for i in range(len(ls)):
        new_ls = ls[i].split()
        # print(new_ls)
        for j in range(len(new_ls)):
            frequency = new_ls.count(new_ls[j])
            print(frequency)
            counter_dict[new_ls[j]] = frequency
    print(counter_dict)



counter(Input_list)

# output  {'Python': 1, 'is': 1, 'a': 1, 'powerful': 1, 'programming': 1, 'language': 1, 'used': 1, 'for': 1, 'web': 1, 'development': 1, 'has': 1, 'rich': 1, 'set': 1, 'of': 1, 'libraries': 1}