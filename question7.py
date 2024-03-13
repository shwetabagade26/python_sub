# manage a dictionary of student records for a school
TF = 1
data_dict = {1:['smith','computer',[23,45,65,77]]}
l_marks = []
choice = int(input(f"""
                    option 1 : ADD \n
                    option 2 : REMOVE \n
                    option 3 : UPDATE \n
                    option 4 : RETRIEVE \n
                    option 5 : DISPLAY \n
                    option 6 : AVG MARKS \n
                    option 7 : EXIT \n
                   Enter your choice:::  """))

if choice == 1: #add
    roll_num = int(input("Enter roll number: "))
    name = input("Enter name:  ")
    clas = int(input("Enter class in integer: "))
    print("Enter marks of 4 subjects English , Maths , Science , CS in order")
    for i in range(4):
        marks = int(input("Enter marks: "))
        l_marks.append(marks)
    data_dict = {roll_num : [name , clas , l_marks]}
    print(data_dict)
elif choice == 2: #remove
        roll_num = int(input("Enter the roll_num to remove data"))
        data_dict.pop(roll_num)
        
elif choice == 3: #update
    roll_num =  roll_num = int(input("Enter the roll_num to update data"))
    data_dict.pop(roll_num)
    # data_dict.update()
elif choice == 4: #retrive
     roll_num =  roll_num = int(input("Enter the roll_num to update data"))
     data_dict.items(roll_num)
elif choice == 5: #display
    print(data_dict)
elif choice == 6: #avg_marks
     print(sum(l_marks))
    
else:
    print("Invalid choice!!")

# print(data_dict)