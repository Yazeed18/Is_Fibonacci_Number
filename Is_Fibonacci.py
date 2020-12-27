import math

x = int(input("Enter a number: "))

if x == 0:
    print("0 is in the Fibonacci Sequence!")
else:
    #RECALL
    #for a number x that if and only if result of 5x^2+4 or 5x^2-4 or both is a
    #perfect square then x is said to be in the Fibonacci Square
    number_1 = ( 5 * (x**2) ) + 4 
    #OR 
    number_2 = ( 5 * (x**2) ) - 4

    root_number_1 = math.sqrt(number_1)
    #OR
    root_number_2 = math.sqrt(number_2)
    
    if root_number_1.is_integer() == True:
        print("%d is in the Fibonacci Sequence!" %(x))
    elif root_number_2.is_integer() == True:
        print("%d is in the Fibonacci Sequence!" %(x))
    else:
        print("%d is not in the Fibonacci Sequence." %(x))
