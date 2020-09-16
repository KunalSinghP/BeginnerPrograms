def func2(): #Function is made, to prevent rewriting in case we need this code at several other places.
   num = int(input('Enter Any Number-'))
   factorial = 1
   i=1
   if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
   elif num == 0:
       print("The factorial of 0 is 1")
   else:
       while i<=num:
          factorial*=i
          i+=1
       print("The factorial of",num,"is",factorial)
func2() #Code won't be executed if we dont call this function.
