balance=1000.0
while True:
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    user_input=int(input("Enter your choise(1-4):"))
    if (user_input==1):
        print("Your current balance is Rs.",balance)
    elif(user_input==2):
        d_amount=float(input("Enter amount to deposit:"))
        balance=balance+d_amount
        print("✅ Deposit Successful!")
    elif(user_input==3):
        w_amount=float(input("Enter amount to withdraw:"))
        if(w_amount>balance):
            print("❌Insufficient funds!")
        else:
            balance=balance-w_amount
            print("✅ Withdrawal Successful!")
    elif(user_input==4):
        print("Thank you for using the ATM")
        break
    else:
        print("❌Invalid choice. Plese try again.")



    
        