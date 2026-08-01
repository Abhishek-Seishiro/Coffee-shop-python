class Account:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a valid amount!")
        else:
            self.balance += amount
            self.history.append(f"Deposited ₹{amount}")
            print(f"₹{amount} deposited successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew ₹{amount}")
            print(f"₹{amount} withdrawn successfully!")

    def show_history(self):
        if not self.history:
            print("\nNo transactions yet!")
        else:
            print("\nTransaction History:")
            for i, record in enumerate(self.history, 1):
                print(f"  {i}. {record}")


class ATM:
    def __init__(self):
        self.accounts = {
            "9876": Account("$outh$ide$suicide", "9876", 790000),
            "5432": Account("Northwest", "5432", 67000),
        }

    def login(self):
        print("\nWelcome to Abhishek dungeon")
        print("=" * 30)
        pin = input("Enter your PIN: ")

        if pin in self.accounts:
            print(f"\nHello, {self.accounts[pin].name}!")
            return self.accounts[pin]
        else:
            print("Wrong PIN! Access Denied.")
            return None

    def run(self):
        account = self.login()

        if not account:
            return

        while True:
            print("\n--- MENU ---")
            print("1-> Check Balance")
            print("2-> Deposit")
            print("3-> Withdraw")
            print("4-> Transaction History")
            print("5-> Exit")

            choice = input("\nChoose an option: ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                amount = int(input("Enter amount to deposit: ₹"))
                account.deposit(amount)
            elif choice == "3":
                amount = int(input("Enter amount to withdraw: ₹"))
                account.withdraw(amount)
            elif choice == "4":
                account.show_history()
            elif choice == "5":
                print("\nThank you for using Abhishek dungeon, Goodbye!")
                break
            else:
                print("Invalid option! Try again.")


atm = ATM()
atm.run()
