# round values for each item present in the list using map function
Input_list = [2.6743, 3.63526, 4.2325, 5.9687967, 6.3265, 7.6988, 8.232, 9.6907 ]
print("Using list comprehension   ",[round(i) for i in Input_list])
print("Using Map Function         ",list(map(round,Input_list)))