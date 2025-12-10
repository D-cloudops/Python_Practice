def mul(a,b):
    try:
      return (a*b)
    except ZeroDivisionError:
        return "Enter a non-zero denominator"


def div(a,b):
    try:
      return (a/b)
    except ZeroDivisionError:
        return "Enter a non-zero denominator"

def main():
    num1=int(input("enter a number " ))
    num2=int(input("enter another number " ))
    operation=input("enter the operator mul or divide ")
    if operation=="mul":
        result=mul(num1,num2)
        print (result)
    else:
        result=div(num1,num2)
        print (result)

if __name__ == "__main__":
    main()