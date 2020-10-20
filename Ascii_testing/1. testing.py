from ascii_value import *
from factorial import factorial
from fibannaci_series import *
from amstrong_number import *
from Odd_or_Even import *

num = int(input("The following opertaion can be done by this compiler : \n 1. ACSII Value \n 2. Factorial \n 3. Fibannaci Series \n 4. Amstrong Number \n 5. Odd or Even \n Enter the Module to use : "))

for i in range (100) :
    if num == 1 :
        s=input("enter the letter : ")
        asc_value(s)
    elif num ==2 :
        s=int(input("enter the value : " ))
        factorial(s)
    elif num == 3 :
        s = int(input("enter the fibanic series : "))
        fibannaci_series(s)
    elif num == 4 :
        s= input("enter the number to check amstrong are not : ")
        amstrong_number(s)
    elif num == 5 :
        s= int(input ("Enter the number : "))
        odd_or_even(s)
    elif num == 0 :
        break 
    num = int (input ("Enter the Module Again (Enter 0 to exit the Compiler) : ")) 
print ("Thank you for using the compiler \n Bye-Bye")