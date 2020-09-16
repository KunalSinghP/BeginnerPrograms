import time #To make it look professional as it takes time to validate id and password

d={'kunal':'ks','yash':'yc'} #Some already made records just to check the login system

for i in range(3): #To give user 3 attempts to login in case he enters wrong credentials
    x=input('Enter UserID:')
    y=input('Password:')
    time.sleep(2)
    if x in d:
        if d[x]==y:
            print('You are logged in.' )
            break #If the credentials is correct, break will end the loop, otherwise the loop will run for 3 times even if u login on your first attempt.
        else:
            print('Wrong Password')
    else:
        print('No such account found')
else:
    print('Sorry. You have tried 3 times and failed to log in.')
