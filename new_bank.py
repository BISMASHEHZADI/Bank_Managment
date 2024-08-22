class Member_Add:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount
        print(f'Amount added successfully. You have added {amount} to your account. New balance is {self.balance}')

    def withdraw_amo(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'You have withdrawn {amount} from your account. New balance is {self.balance}')
        else:
            print('Insufficient balance')

    def show(self):
        print(f'Member name: {self.name}, Member account no: {self.acc_no}, and balance is {self.balance}')


class Bank:
    def __init__(self):
        self.members = {}

    def add_member(self, acc_no, name, balance):
        if acc_no in self.members:
            print('Account already exists')
            # return
        self.members[acc_no] = Member_Add(acc_no, name, balance)
        
        print('Member added successfully')

    def member_view(self, acc_no):
        member = self.members.get(acc_no)
        if member:
            member.show()
        else:
            print('Account not found')

    def deposit_acc(self, acc_no, amount):
        member = self.members.get(acc_no)
        if member:
            member.add_money(amount)
        else:
            print('Account not found')

    def withdraw_acc(self, acc_no, amount):
        member = self.members.get(acc_no)
        if member:
            member.withdraw_amo(amount)
        else:
            print('Account not found')


# Example usage with user input
bank = Bank()


while True:
    print("""
    Menu
    1.Add member
    2.View member
    3.deposit
    4.withdraw 
    5.exit


    
    
    
    """)
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        acc_no = input("Enter account number: ")
        name = input("Enter member name: ")
        balance = float(input("Enter initial balance: "))
        bank.add_member(acc_no, name, balance)
    
    elif choice == '2':
        acc_no = input("Enter account number: ")
        bank.member_view(acc_no)
    
    elif choice == '3':
        acc_no = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        bank.deposit_acc(acc_no, amount)
    
    elif choice == '4':
        acc_no = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        bank.withdraw_acc(acc_no, amount)
    
    elif choice == '5':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
