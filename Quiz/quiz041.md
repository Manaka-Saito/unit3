# This is quiz 041
<img width="800" alt="Screenshot 2025-02-24 at 23 44 00" src="https://github.com/user-attachments/assets/32e83042-1494-4a6d-bac4-aeaddddc566b" />


## Code
```py

import sqlite3
from contextlib import nullcontext

from kivy.lang import Builder
from kivymd.app import MDApp
from quiz_040password_encryption import encrypt_password, check_hash

class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


class quiz040(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.components = {"base":0, 'inhabitant': 0, 'income': 0, 'pension': 0, 'health': 0, 'total': 0, 'hash': ''}
        self.encrypt_amount = ''

    def build(self):
        return Builder.load_file('quiz040.kv')

    def save(self):
        pass

    def update(self):
        #This function updates all the labels in the form using the base salary and the percentage
        # Pseudocode
        # 1- get the base salary from the GUI
        base = self.root.ids.base.text
        # 2- if base salary define total=int(base) and an empty string to store build a hash (for_hash="")
        # if no base then end the function
        if base:
            for_hash = ''
            total = int(base)
            gross_salary = total
            for_hash += f"base{total},"
            print(f"{total}")
            # 3- for Each TextField with ids: "inhabitant","income_tax","pension","health" get the text property
            for ids in ["inhabitant", 'income_tax', 'pension', 'health']:
                amount = self.root.ids[ids].text
                # 4- if the TextField.text has a number (value),
                # calculate the equation new_value="(base*int(value)//100) JPY" and subtract the equation to the total
                if amount:
                    new_value = (total*int(amount)//100)
                    self.root.ids[ids+"_label"].text = f"{new_value} JPY"
                    for_hash += f"{ids}{new_value},"
                    gross_salary -= new_value
                # 5- if no: then new_value = " JPY"
                else:
                    new_value = "JPY"
                # 6- set the label next to the TextField (inhabitant_label, income_tax_label, etc) to the variable new_value

                self.root.ids[f"{ids}_label"].text = f"{new_value} JPY"
                # 7- concatenate to the hash variable the f"{id}{value}"
                for_hash += f"{id}{amount}"
            # 8- set the text of the element id=total to the total with the JPY symbol
            self.root.ids.salary_label.text = f"{gross_salary} JPY"

            # 9- encrypt the hash and change the text of the label with id=hash to the last 50 characters of the hash
            encrypt_amount = encrypt_password(str(gross_salary))
            last_50 = encrypt_amount[-50:]
            self.root.ids.hash.text = last_50

    def save(self):
        #repeat the algorithm in update but create variables to save the amount of each item:
        base = self.components['base']
        inhabitant = self.components['inhabitant']
        income_tax = self.components['income']
        pension = self.components['pension']
        health = self.components['health']
        total = self.components['total']
        hash = self.encrypt_amount

        #inhabitant4,income_tax3,pension2,health1,total1103  (here the numbers next to the category are percentages)

        query = f"""INSERT into payments('base', 'inhabitant', 'income_tax', 'pension', 'health',
        'total', 'hash') VALUES ({base}, {inhabitant}, {income_tax}, {pension},{health},{total},'{hash}')
         """
        db = database_worker("payments.db")
        db.run_save(query)
        db.close()
        self.root.ids.hash.text = f"Payment saved"

    def clear(self):
        for label in ["base", "inhabitant","income_tax","pension","health"]:
            self.root.ids[label].text = ""
            self.root.ids[label+"_label"].text = " JPY"

        self.root.ids["salary_label"].text = " JPY"
        self.root.ids.hash.text = "----"


test = quiz040()
create = """CREATE TABLE if not exists payments(
        id INTEGER PRIMARY KEY,
        base INTEGER,
        inhabitant INTEGER,
        income_tax INTEGER,
        pension INTEGER,
        health INTEGER,
        total INTEGER,
        hash TEXT
     )"""
db = database_worker("payments.db")
db.run_save(create)
db.close()
test.run()

```


## Proof of Work

https://github.com/user-attachments/assets/d9a470aa-15e6-4246-bfad-60008be7edb0
