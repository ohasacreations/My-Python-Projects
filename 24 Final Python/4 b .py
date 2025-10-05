from datetime import date
today = date.today()


file=open('Account.txt','a+')
file.seek(0,0)
line=((file.readline()).strip()).split('/')
balance=int(line[2])




AccNo=input("Enter the Account number")
while True:
    user_input=input("Enter the Code: ")
    if (user_input=='0'):
        break
    else:
        digit=AccNo[0]
        Amount=int(user_input[1:])
        if(digit=="D"):
            balance-=Amount
        else:
            balance+=Amount
file.write(f"\n{today}/{AccNo}/{balance}")
file.close()
