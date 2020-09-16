d={}
n=int(input("Number of student records to be entered:"))
for i in range(n):
    x=int(input('Enter Roll No.:'))
    y=input("Name:")
    z=input("Stream:")
    a=input("Class:")
    fj=(y,z,a)
    d[x]=fj
m=int(input("Enter Roll Number to see details of a student:"))
z=d[m]
print("Name\t""Stream\t""Class\t")
for i in z:
    print(i,end="\t")
    
    
