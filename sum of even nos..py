n=int(input("Please Enter the maximum limit upto which you want the sum-"))
t = 0
x = 1

while x<=n:
    if(x%2 == 0):
        print("{0}".format(x))
        t=t+x
    x=x+1
print("The sum of even nos. from 0 to ",n,"=" " {0}".format(t))
