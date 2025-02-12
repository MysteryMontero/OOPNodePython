from account import (
    SavingsAccount, CheckingAccount, HighInterestSavingsAccount,
    OverdraftCheckingAccount, PremiumOverdraftCheckingAccount
)

def main():
    # Create and interact with accounts
    savings = SavingsAccount("12345", "Steven Bills", 1000)
    premium = PremiumOverdraftCheckingAccount("67890", "Spongebob Squarepants", 2000)

    # perform some operations
    savings.deposit(500)
    premium.withdraw(250)
    premium.deposit(1000)

    # display balances
    savings.display_balance()
    premium.display_balance()

if __name__ == "__main__":
    main()
