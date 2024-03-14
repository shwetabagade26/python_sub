# sqaures of postive numbers,cubes of negative numbers ,absolute values of all integers,even numbers greater than 10

Input_numbers = [5 , -8 , 12,-3,17,0,-10,6,16]

sq_pn = [x**2 for x in Input_numbers if x >= 0 ]
print("Squares of Positive Integers:    ",sq_pn)

cubes_nn = [x**3 for x in Input_numbers if x<0]
print("Cubes of Negative Integers:      ",cubes_nn)

abs_val = [abs(x) for x in Input_numbers]
print("Absolute Values of All Integers: ",abs_val)

even_g10 = [x for x in Input_numbers if x%2 == 0 and x > 10]
print("Even Numbers Greater than 10:    ",even_g10)