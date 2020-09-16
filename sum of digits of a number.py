"""Ex- Input=1234
       Output=1+2+3+4=10"""

n=int(input("Enter Any Number to get the Sum of its digits-"))
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print(s)
