x=int(input("enter Starting daily calorie intake."))
y=int(input("enter Average daily percentage decrease"))
z=int(input("enter the number of days"))
a=1
while(a<=z):
    print("Day",x)
    x=x+(x*(y/100))
    a=a+1
    