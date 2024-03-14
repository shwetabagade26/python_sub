# frequency of each word in the list and store result in dictionary

Input_list = ["   Python is a powerful programming language",
              "Python is    used for   web development",
              "Python has a rich set of    libraries"]
  

# def counter(ls):  #length of each word
#     counter_dict = {}
#     for i in range(len(ls)):
#         new_ls = ls[i].split()
#         for j in range(len(new_ls)):
#             frequency = len(new_ls[j])
#             counter_dict[new_ls[j]] = frequency
#     print(counter_dict)

# def counter(ls): #counts separately for each item in the list
#     counter_dict = {}
#     new_ls=str(Input_list)
#     print(new_ls)
#     for i in range(len(ls)):
#         new_ls = ls[i].split()
#         # print(new_ls)
#         for j in range(len(new_ls)):
#             frequency = new_ls.count(new_ls[j])
#             print(frequency)
#             counter_dict[new_ls[j]] = frequency
#     print(counter_dict)


def word_frequency(sentences): 
    #frequency of words in a sentence 
    word_count = {}
    for sentence in sentences:
        words = sentence.split()
        for word in words: # if key repeats add one 
            word_count[word] = word_count.get(word, 0) + 1
    print(word_count)

    

# counter(Input_list)
word_frequency(Input_list)