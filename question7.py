# manage a dictionary of student records for a school
TF = 1
data_dict = {1:['smith','computer',[23,45,65,77]]}
l_marks = []

while True:
    choice = int(input(f"""
            ===================================
                    option 1 : ADD 
                    option 2 : REMOVE 
                    option 3 : UPDATE 
                    option 4 : RETRIEVE 
                    option 5 : DISPLAY 
                    option 6 : AVG MARKS 
                    option 7 : EXIT 
            ===================================\n
                   Enter your choice:::  """))
    if choice == 1: #add
        roll_num = int(input("Enter roll number: "))
        name = input("Enter name:  ")
        clas = int(input("Enter class in integer: "))
        print("Enter marks of 4 subjects (total marks 100): ")
        sub = ['English','Maths','Science', 'CS']
        for i in range(4):
            marks = int(input(f'Enter marks of {sub[i]}: '))
            l_marks.append(marks)
            data_dict.update({roll_num:[name , clas , l_marks]})
            # data_dict = {roll_num : [name , clas , l_marks]}
        print(data_dict)
    elif choice == 2: #remove
            roll_num = int(input("Enter the roll_num to remove data:  "))
            data_dict.pop(roll_num)
            print("Student Value  removed!!")
            
    elif choice == 3: #update
        choice1 = int(input(f"""
            ===================================
                    Roll no (cant be updated unique) \n
                    option 1 : name 
                    option 2 : class 
                            MARKS \n
                    option 3 : English
                    option 4 : Maths
                    option 5 : Science 
                    option 6 : CS 
            ===================================\n
                   Enter your choice:::  """))
        roll_num = int(input("Enter the roll_num to update data:  "))
        if choice1 == 1:
            name = input("Enter new value for name:  ")
            data_dict.update({roll_num:[name , clas , l_marks]})
        elif choice1 == 2:
            clas = int(input("Enter  new value for class:  "))
            data_dict.update({roll_num:[name , clas , l_marks]})
        elif choice1 == 3:
            english = int(input("Enter new value for English:  "))
            l_marks[0] = english 
            data_dict.update({roll_num:[name , clas , l_marks]})
        elif choice1 == 4:
            maths = int(input("Enter new value for maths:  "))
            l_marks[1] = maths
            data_dict.update({roll_num:[name , clas , l_marks]})
        elif choice1 == 5:
            science = int(input("Enter new value for science:  "))
            l_marks[2] = science
            data_dict.update({roll_num:[name , clas , l_marks]}) 
        elif choice1 == 6 : 
            cs = int(input("Enter new value for CS :  "))
            l_marks[3] = cs
            data_dict.update({roll_num:[name , clas , l_marks]})

        print("Student Info  updated!!")

    elif choice == 4: #retrive
        roll_num =  roll_num = int(input("Ente the roll number to fetch the data:  "))
        print(data_dict.items())

    elif choice == 5: #display
        print("\n\t\t",data_dict,"\t\t\n")
        
    elif choice == 6: #avg_marks
        print("\t\t Average Marks \t",sum(l_marks)/len(l_marks),"\t\t")
    
    elif choice == 7 :
        break
    else:
        print("Invalid choice!!")

# print(data_dict)