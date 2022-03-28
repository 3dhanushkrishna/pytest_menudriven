def square(x):
    return x ** 2

def perimeter(x,y):
    return 2*(x+y)

def rectangle(x,y):
    return x*y
if __name__=="__main__":


   while True:
    print("select the option: ")
    print("1. area of square: ")
    print("2. perimeter of rectangle: ")
    print("3. area of rectangle: ")
    print("4.exit")
    option=int(input("select the option"))

    if option==1:
        x=int(input("enter the value: "))
        areasquare=square(x)
        print(areasquare)
    elif option==2:

        x=int(input("enter the length:"))
        y=int(input("enter the breadth:"))
        perirectangle=perimeter(x,y)
        print(perirectangle)
    elif option==3:


        x = int(input("enter the length:"))
        y = int(input("enter the breadth:"))
        arerectangle=rectangle(x,y)
        print(arerectangle)
    elif option==4:
        break
    else:
        print("invaild option")

