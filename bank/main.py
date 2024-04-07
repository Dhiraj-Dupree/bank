class Bank:
      def __init__(self):
            self.balance = 300
            self.transactions = []
            self.options = {
                  '1': self.show_transactions,
                  '2': self.withdraw,
                  '3': self.deposit,
                  '4': exit
                  }
            
      def show_transactions(self):
            print("past transactions:")
            for transaction in self.transactions:
                  print(transaction)
           
                  
      def withdraw(self):
            amount = float(input('How much would you like to withdraw: '))
            if amount <= self.balance:
                  self.balance -= amount
                  self.transactions.append(f'withdrawn: ${amount:.2f}')
                  print(f'New Balance; ${self.balance:.2f}')
            else:
                  print('invalid amount, check your balance and try again')
                  
            
      def deposit(self):
            amount = float(input('how much would you like to deposit: '))
            self.balance += amount
            self.transactions.append(f'Deposited: ${amount:.2f}')
            print(f'New Balance: ${self.balance:.2f}')
            
      
      def main(self):
            while True:
                  choice = input('''
welcome, chose what you'd like to do
(1) show transactions
(2) withdraw
(3) deposit
(4) exit                             

Choice: ''').strip()
                  if choice in self.options:
                        self.options[choice]()
                  else:
                        print('invalid choice')
                  
if __name__ == '__main__':
      bank = Bank()
      bank.main()
            
            
            