#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize the CashRegister object with a discount (default is 0)
        self.discount = discount
        self.total = 0  # Initialize total amount to zero
        self.items = []  # Initialize list to store items
        self.previous_transactions = []  # Initialize list to store previous transactions

    def add_item(self, item, price, quantity=1):
        # Add an item to the register with specified price and quantity
        self.total += price * quantity  # Update total amount
        for _ in range(quantity):  # Add each item to the list of items
            self.items.append(item)
        # Add details of the transaction (item, price, quantity) to previous_transactions
        self.previous_transactions.append([item, price, quantity])

    def apply_discount(self):
        # Apply discount to the total amount if a discount is specified
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))  # Calculate discounted total
            print(f"After the discount, the total comes to ${self.total}.")  # Print discounted total
        else:
            print("There is no discount to apply.")  # Print message if no discount is applied

    def void_last_transaction(self):
        # Void the last transaction by removing it from previous_transactions
        if not self.previous_transactions:  # Check if there are any transactions
            return "There are no transactions to void."  # Return message if no transactions
        last_tranaction = self.previous_transactions.pop()  # Remove last transaction
        self.total -= last_tranaction[1] * last_tranaction[2]  # Deduct the total amount of the last transaction
        for _ in range(last_tranaction[2]):  # Remove each item of the last transaction from the list of items
            self.items.pop()
