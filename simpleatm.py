def main ():
    #user data
    accountHoldersName = ["harry den", "david beckingham", "tom reidy", "emma reidy", "kate reidy"]
    pinCode = ["1234", "1999", "2424", "1985", "5555"]
    accountNumber = ['1353', '199281', "182838", "185597", "667432"]
    balance = [567000, 21873, 2341871, 275638, 91820]

    #loop
    while True: #so the loop runs almost infinit many times
        print("\t\t=== Welcome To Simple ATM System ===")

        #login details and account name validation 
        while True:  
            account = input("Enter Your Name: ")
            account= account.lower() 
            if account in accountHoldersName:
                  break
            else:
                print("Account does not exist")

        #gets acount details using index
        index = accountHoldersName.index(account)
        #validate pin
        pin = input("Enter your Pin:")
        if pin != pinCode[index]:
            print("Incorrect Pin try again")
        else:
            print("Your account number is ",accountNumber[index])
            print("Your balance is £",balance[index])

        # ask user to withdraw or deposit
        withdrawOrDeposit = input("Do you want to withdraw, deposit or no: ")
        withdrawOrDeposit= withdrawOrDeposit.lower()
        if withdrawOrDeposit == "withdraw":
                amount = float(input("Enter the amount you want to draw (numbers only):"))
                finalAmount = balance[index] - amount
                print("Thank you for using this Simple ATM System. Brought To You By TomTom")
                balance.remove(balance[index])
                balance.insert(index, finalAmount)
                print("Your Balance is now £", finalAmount)
        elif withdrawOrDeposit == "deposit":
                amount = float(input("Enter the amount you want to deposit (number only):"))
                finalAmount = balance[index] + amount
                print("Thank you for using this Simple ATM System. Brought To You By TomTom")
                balance.remove(balance[index])
                balance.insert(index, finalAmount)
                print("Your Balance is now £",finalAmount)
        else:
                print("Thank you for using this Simple ATM System. Brought To You By TomTom")
      
main()