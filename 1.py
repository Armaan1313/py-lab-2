x=int(input("enter number of years you want to calculate"))
while(x>0):
    b=12
    total=0
    average=0
    while (b>0):
        y=int(input("enter the input for calculating average high temperature for each month."))
        total=total+y
        b=b-1
    print("total=",total)
    print("average=",total/12)
    x=x-1