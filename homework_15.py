
class BankSystem:

    bank_name = "Bank of Georgia"
    __total_accounts = 0

    @staticmethod
    def validate_amount(amount):
        return amount > 0
    
    @classmethod
    def get_total_accounts(cls):
        return f'There are total of {cls.__total_accounts} accounts.'
    
    def __init__(self, owner, balance):
        BankSystem.__total_accounts += 1
        
        self._owner = owner
        
        if BankSystem.validate_amount(balance):
            self.__balance = balance
        else:
            self.__balance = 0

        self.__account_number = f'AN{BankSystem.__total_accounts:04d}'

    # ბალანსზე თანხის დამატება
    def deposit(self, amount):
        if BankSystem.validate_amount(amount):
            self.__balance += amount
            print(f'{self.__account_number}: {amount}GEL is deposited.')
        else:
            print('Amount is not valid.')

    # ბალანსიდან თანხის გამოტანა
    def withdraw(self, amount):     
        if BankSystem.validate_amount(amount):
            if self.__balance >= amount:
                self.__balance -= amount
                print(f'{self.__account_number}: {amount}GEL is Withdrawed.')
            else:
                print(f'There is not enough money on this account.')
        else:
            print('Amount is not valid.')


    def check_balance(self):
        return f'Balance: {self.__balance}GEL'

    def get_account_number(self):
        return f'Account number is: {self.__account_number}'

    def change_owner(self, new_owner):
        self._owner = new_owner
        print(f'Owner has been changed. New owner: {new_owner}')
        return

    def __str__(self):
        # "Account: AN0002 | Owner: Nino Beridze"
        return f'Account: {self.__account_number} | Owner: {self._owner}'
    
    
# test
account1 = BankSystem("Otar Tumanishvili", 15000)
print(account1)
account2 = BankSystem("Nino Beridze", 2000)
print(account2)
account3 = BankSystem("Test Subject", -100)
print(account3)
print(BankSystem.get_total_accounts())

account1.deposit(250)
account2.withdraw(100)
account3.deposit(-100)
account3.withdraw(-50)
print(account1.check_balance())
print(account2.check_balance())
print(account3.check_balance())

account2.change_owner("Nino Aptsiauri")
print(account2)

#wrong withdraw 
account2.withdraw(2500)
