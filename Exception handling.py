'''a,b=5,0
try:
    print("resource opened")
    print(a/b)
    k=int(input("enter any num"))
    print(k)

except ZeroDivisionError as e:
    print(" hey can't div by 0",e)

except ValueError as e:
    print("Invalid input",e)

except Exception as e:
    print("Oops!something went wong",e)

finally:
    print("resource closed")'''

#--------------------------------


def handling(a,b):


    try:
         c=a/b
         print(c)

    except ZeroDivisionError as e:
        print("can't div by 0",e)

    except NameError as e:
        print("Invalid input", e)

    except Exception as e:
        print("Oops!something went wong", e)

    else:
        print("This runs only when except doesn't run")

    finally:
        print("The solution is printed")


handling(6,0)










