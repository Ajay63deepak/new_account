def fibannaci_series(s) :
    sum = [0,1]
    for i in range (s-2) :
        series = int(sum[-1]) + int(sum[-2])
        sum.append(series)
        i+=0
    print("The fibanacci series are : "+ str(sum))