# This is quiz 040
<img width="max" alt="Screenshot 2025-02-24 at 19 27 57" src="https://github.com/user-attachments/assets/ee3d3336-e12b-41c0-acc4-6f9c566022c6" />


## UML Diagram
![IMG_1689](https://github.com/user-attachments/assets/fcb81ba8-d358-4e7c-bba4-112da2f41719)


## Code

```py

import sqlite3
from mylib import databaseManager


class InvestigateSus:
    def __init__(self):
        self.current_balance_list = []
        self.transaction_list = []
        self.db = databaseManager('smallCase.db')

    def get_data(self):
        query = """SELECT transaction_id, amount from transactions where transaction_id <= 20"""
        current_balance = self.db.search(query)
        self.current_balance_list = [list(balance) for balance in current_balance]

        query = """SELECT account_id, amount FROM transactions WHERE transaction_id > 20"""
        self.transaction_list = self.db.search(query)

    def find_suspect(self):
        self.get_data()
        answer = 0
        for transaction in self.transaction_list:
            for i in self.current_balance_list:
                if transaction[0] == i[0]:
                    i[1] -= transaction[1]
                    if i[1] < 0:
                        answer = transaction[0]

        query = f"""SELECT first_name, last_name from customers WHERE customer_id = {answer}"""
        details = self.db.search(query)
        return f"{details[0][0]} {details[0][1]} was the cause of bankrupt."

    def close_db(self):
        self.db.close()

output = InvestigateSus().find_suspect()
print(output)

```
## Proof of Work

<img width="1050" alt="Screenshot 2025-02-25 at 20 02 17" src="https://github.com/user-attachments/assets/563919dc-0531-4b65-991a-67c21813e93a" />
