import math

def amstrong_number(s) :
    sum = 0
    for i in range (len(s)) :
        exp = int(s[i-1]) ** len(s)
        sum = sum + exp
        print(sum)
    if sum == int(s) :
        print ("it is amstronag number")
    else :
        print("it is not a amstrong number")

def asc_value(a) : 
    print ("The ASCII value of " + a +" is " + str(ord(a)))

def factorial(a) :
    print("The factorial of "+str(a)+" is "+str(math.factorial(a)))

def fibannaci_series(s) :
    sum = [0,1]
    for i in range (s-2) :
        series = int(sum[-1]) + int(sum[-2])
        sum.append(series)
        i+=0
    print("The fibanacci series are : "+ str(sum))

def odd_or_even (s) :
    print("this is even") if s % 2==0 else print("this is odd")