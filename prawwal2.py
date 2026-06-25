#to be updated
account = {}
print("welcome to our bank")
while True :
    print("1.create account")
    print("2.deposite ")
    print("3.withdraw")
    print("4.check balance")
    print("5.exit")

    choice = input("enter your choice : ").strip()
    
    if choice == '1':
        name = input("enter your name : ").strip()
        
        if name in account:
            print("account already exists")
        else:
            account[name] = 0.0
            print("account added for ", name)
            
    
    elif choice == '2':
        name = input("enter account holders name :").strip()
        
        if name not in account :
            print("account does not exist ")
            continue
        
        try:
            amount= float(input("enter deposite amount:"))
            if amount <= 0:
                print("amount must be greater then zero ")
            else :
                account[name] += amount
                print("₹", amount, "deposited successfully")
        except ValueError:
            print("invalid amount. please enter a valid number.")
    
    elif choice == '3':
        name = input("enter account holder name :").strip()
        
        if name not in account:
            print("account not found ")
            continue
        try:
            amount = float(input("enter withdrawal amount:"))
            if amount <= 0:
                print("amount must be greater then zero ")
            elif amount > account[name]:
                print("insufficient balance")   
            else:
                account[name] -= amount
                print("₹", amount, "withdrawn successfully")
        except ValueError:
            print("invalid amount. please enter a valid number.")
   
    elif choice == '4':
        name = input("enter account holder name :").strip()
        
        if name not in account:
            print("account not found ")
        else:
            print("current balance for", name, "is ₹", account[name])
    
    elif choice == '5':
        print("thank you for using our bank")
        break
    else:
        print("invalid choice. please try again.")
