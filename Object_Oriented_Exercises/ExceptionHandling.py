
def first():
    try:
        for i in ['a','b','c']:
            print(i**2)
    except:
        print("Exception is being handled")


def second():
    try:
        x = 5
        y = 0

        z = x / y
    except:
        print("Second exception is being handled")
    finally:
        print("All done")


def ask():
    while(1):
        try:
            var = int(input("Type a number: "))
            print("The square of the number is: ", var**2)
        except:
            print("Third exception is being handled")
        else:
            print("Number is correct")
            break
        finally:
            print("Second all done")


if __name__ == '__main__':
    print("Running")
    ask()