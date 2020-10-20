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