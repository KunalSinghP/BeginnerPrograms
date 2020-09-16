L1=['orange','blue','red','yellow']
l='y'
while l=='y':
    x=input("Enter the colour you want to add in the list: \n")
    if x in L1:
        print("Colour is already there in the list")
        p=input("Enter 'a' add it again or enter 'y' to add any other colour or enter 'x' to exit:")
        if p=='a':
            L1.append(x)
            print(L1)
            l=input("Enter 'y' to add any other colour or 'x' to exit:")
        elif p=='y':
            l=p
            print(L1)
        elif p=='x':
            exit()
    if x not in L1:
        L1.append(x)
        print(L1)
        l=input("Enter 'y' to add any other colour or 'x' to exit:")
else:
    exit()
