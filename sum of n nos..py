"""If you give 4 as input, you will get sum of numbers upto 4 which is 1+2+3+4=10"""

def func1():
    num=int(input('Enter Any Natural Number'))
    s=0
    if (num>0):
        for i in range(1,num+1):
            s=s+i
        print(s)
    else:
        print(num,'is not a natural number')
func1()
        
     














    


