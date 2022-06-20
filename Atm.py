from ctypes.wintypes import PINT


class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("Your balance is: $13500")

    def cashwidthdrawal(self, amount):
        new_amount = 13500-amount
        print("You widthdrawed: " + str(amount)+ "Your remaining balance is:" + str(new_amount))

def main():
        name = input("Hello! What is your name?")
        print("Hello", name)
        cardnumber = input("Insert your card number: ")
        pin = input("Enter your pin: ")
        new_user = Atm(cardnumber, pin)

        print("Choose activity")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawel")
        activity = int(input("Enter activity choise: "))

        if(activity == 1):
            new_user.balanceinquiry()
        elif (activity == 2):
            amount = int("Enter the amount: ")
            new_user.cashwidthdrawal(amount)
        else:
            print("Enter a valid number")
        
if __name__== "__main__":
    main()