d={'kunal':'ks','yash':'yc'}
for i in range(3):
    x=input('Enter UserID:')
    y=input('Password:')
    if x in d:
        if d[x]==y:
            print('You are logged in.' )
            break
        else:
            print('Wrong Password')
    else:
        print('No such account found')
else:
    print('Sorry. You have tried 3 times and failed to log in.')
