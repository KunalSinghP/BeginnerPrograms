a=float(input('Enter Your Marks In 1st Subject'))
b=float(input('Enter Your Marks In 2nd Subject'))
c=float(input('Enter Your Marks In 3rd Subject'))
d=float(input('Enter Your Marks In 4th Subject'))
e=float(input('Enter Your Marks In 5th Subject'))
Avg=(a+b+c+d+e)/5
print('Your Average Marks is ',Avg)
if (Avg>=90):
    P='A+'

elif(Avg>=80):
    P='A'

elif(Avg>=70):
    P='B+'

elif(Avg>=60):
    P='B'

elif(Avg>=50):
    P='C+'

elif(Avg>=40):
    P='C'

elif(Avg<40):
    P='FAIL'

print('Your Grade is ',P)
