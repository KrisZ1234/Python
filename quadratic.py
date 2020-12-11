import math

print("------ a*x**2 + b*x + c = 0 ------- ")

inp1_str = input("Type a -> ")
inp2_str = input("Type b -> ")
inp3_str = input("Type c -> ")

def solutions(a,b,c):
    """ inputs: 3 float numbers
    Does the proper calculations (for ALL scenarios)
    and prints the solutions """
    
    D = (b**2) - (4*a*c)
    
    if D > 0:
        if a == 0 and b != 0 and c == 0:
            print('Solution: x=',0)
        elif a == 0 and b != 0 and c != 0:
            print("Solution: x=",-c/b)
        else:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            print("Solutions: x1=",x1)
            print("           x2=",x2)
            
    elif D == 0:
        if a == 0 and b == 0 and c != 0:
            print("Incorrect equation,",c,"= 0")
        elif a != 0 and b == 0 and c == 0:
            print('Solution: x=',0)
        elif a == 0 and b == 0 and c == 0:
            print("Infinite solutions")
        else:
            x = -b / (2*a)
            print("Solution: x=",x)
            
    else:
        print("No real Solutions")
        
""" check if the inputs are correct 
       and procedes to the solution """
       
if inp1_str and inp2_str and inp3_str: 
    try:
        inp1 = float(inp1_str)
        inp2 = float(inp2_str)
        inp3 = float(inp3_str)
        solutions(inp1,inp2,inp3)
    except:
        print()
        print ("Incorrect inputs!!")
        
else:
    print("Not enough inputs!!")
