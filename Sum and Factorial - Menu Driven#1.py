#Menu driven program means you have two or more choices of performing different actions in one program like we have food choice in a hotel menu

def sum_num():
    """This function gives sum upto n numbers.
    For example: Input:5 then Output=0+1+2+3+4+5=15"""       #This is a docstring
                    
    num=int(input('Enter Any Natural Number-'))
    s=0
    if (num>0):
        for i in range(1,num+1):
            s=s+i
        print(s)
    else:
        print(num,'is not a natural number')

def factorial():
    """This function prints the factorial of the number given as input by the user"""   #This is a docstring
   num = int(input('Enter Any Number-'))
   factorial = 1
   if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
   elif num == 0:
       print("The factorial of 0 is 1")
   else:
       for i in range(1,num + 1):
          factorial*=i
       print("The factorial of",num,"is",factorial)

print('1.Factorial of a Number')
print('2.Sum of n numbers')
a='y'
while a=='y':
    
    r=int(input('Choose the program you want to execute.Press 1 or 2-'))
    if r==1:
        factorial() 
    elif r==2:
        sum_num()
    else:
        print("Sorry We Don't know what you are looking for.BTY this program is for humans.So please check if you are human or not before continuing")
    a=str(input("Enter y if you wish to continue:-"))
else:
    print("ERROR 404:NOT FOUND")
