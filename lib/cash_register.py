#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.all_item = []
    
  def add_item(self, title, price, quantity=1):
    self.title = title
    self.total += price * quantity
    self.all_item.append([title, price, quantity]) 
    for _ in range(quantity):
      self.items.append(title)
      
  def apply_discount(self):
    if self.discount:
      self.total = int(self.total * ((100 - self.discount)/100))
      print(f'After the discount, the total comes to ${self.total}.')
    else:
      print(f'There is no discount to apply.')
      
  def void_last_transaction(self):
    if self.items:
      self.all_item
      print(self.all_item[-1][2])
      for i in range(self.all_item[-1][2]):
        self.items.pop()
      self.total -= self.all_item[-1][1] * self.all_item[-1][2]
      self.all_item.pop()
      
      
    
# CashRegister in cash_register.py takes one optional argument, a discount, on initialization. .                            [  7%]
# CashRegister in cash_register.py sets an instance variable total to zero on initialization. .                             [ 14%]
# CashRegister in cash_register.py sets an instance variable items to empty list on initialization. .                       [ 21%]
# CashRegister in cash_register.py accepts a title and a price and increases the total. .                                   [ 28%]
# CashRegister in cash_register.py also accepts an optional quantity. .                                                     [ 35%]
# CashRegister in cash_register.py doesn"t forget about the previous total .                                                [ 42%]
# CashRegister in cash_register.py applies the discount to the total price. .                                               [ 50%]
# CashRegister in cash_register.py prints success message with updated total .                                              [ 57%]
# CashRegister in cash_register.py reduces the total .                                                                      [ 64%]
# CashRegister in cash_register.py prints a string error message that there is no discount to apply .                       [ 71%]
# CashRegister in cash_register.py returns an array containing all items that have been added .                             [ 78%]
# CashRegister in cash_register.py returns an array containing all items that have been added, including multiples .        [ 85%]
# CashRegister in cash_register.py subtracts the last item from the total .                                                 [ 92%]
# CashRegister in cash_register.py returns the total to 0.0 if all items have been removed .                                [100%]

  
    


