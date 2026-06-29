atm ={
    "reem":5000,
    "zawa":4000
}
pin={
    "reem": 1234,
    "zawa": 5678
}
name = input("Enter your name : ")
user_pin = int (input("enter your pin: "))
if user_pin==pin[name]:
    print("Pin correct")


    if name in atm:
        print("Press key which you wants")
        print('''1 = Balance
2 = Withdraw
3 = Deposit
4= Exit''')
        # balance 
        press = int(input("Enter key: "))
        if press == 1:
            print("Balance =",atm[name])
        # withdraw
        elif press ==2:
            amount =int(input("Enter amount"))
            if amount<= atm[name]:
                if atm[name]-amount< 500:
                    print("Transaction reject")
                else:
                    atm[name] -= amount
                
                    print("Withdraw succesful ")
                    print("Remaining amount is ",atm[name])
            else:
                print("Insufficient Balance ")
        # deposit 
        elif press ==3:
            deposit = int (input("enter your deposit amount : "))
            atm[name]+= deposit
            print ("Your balance:",atm[name])
         # exit
        elif press == 4 :
            print("Thank you")
        # press key invalid
        else:
            print("Invalid choice")
        #name invalid
    else:
        print("User not found ")
        # pin invalid 
else:
    print("Pin wrong")


