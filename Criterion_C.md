# Criterion C


## Techniques Used:

1. If statements ()
2. For loops and While loops for iterating data
3. Hashing and verifying for passwords to protect the personal information
4. Functions to make the application interactive and functional
5. Database to store and retrieve data
6. Input validation 
7. Widgets
8. DatabaseManager


## 1. **Database**
To fulfill the client's request to have a sign up system, **[success criteria 1]** I firstly created a database that is connected to the python file, `main.py`. The **database** is responsible for storing the user information which is essential for creating a registeratino system. Following is the SQL command to create table:
From `main.py`
```python
table = """CREATE table if not exists user(
   id integer primary key,
   username text unique,
   email text unique,
   password varchar(256)
   )
   """
```
This command creates a table called `users` with the columns `id`, `username`, `email`, and `password`. The `id` is a primary key which indicates that it is always unique for each column in the table. `username` is a string that is unique which therefore prevents different users from having two different accounts with the same username which declines in security. `email` is also unique, and `password` is a string that has a maximum length of 256 characters. This is because before storing the password, it will be hashed in order to protect information from malicious users or in case of corruption in the program and information to spread. 

## 2. **Hashing and verifying**
**Hashing and verifying** passwords are the techniques used when storing and retrieving information into a database as indicated above. Following is the code developed to enhance the security of the application.
From  `protectPasswd.py`
```python
from passlib.context import CryptContext
from passlib.hash import sha256_crypt


hash_function = sha256_crypt.using(rounds = 30000)
pwd_config = CryptContext(schemes = ["sha256_crypt"],
                         default = "sha256_crypt")
def check_hash(input_str, hash):
   return pwd_config.verify(input_str, hash)


def encrypt_password(in_password:str):
   return pwd_config.hash(in_password)
```
It imports the Python library, `passlib` and uses a hashing algorithm `sha256_crypt` to hash and verify. `hash_function` indicates that the program uses `sha256_crypt` hash with 30,000 rounds of computation while `pwd_config` is a `CryptContext` object to manage the password hashing and verification. First function takes `input_str`, a string, and `hash`, a string, as arguments, and returns a boolean if the `input_str` and `hash` matches. If they match, it returns True while it returns False if they don’t match. Second function takes `in_password`, a string, as an argument, and returns hashed `in_password` by using `hash_function`. 

## 3. **Functions** / **If Statement** / **Database**
Utilizing those techniques(`database` and `hashing and verifying`), I developed a registration function within `SingUpScreen` using python. 
From `main.py`
```python
   def try_signup(self):
       uname = self.ids.uname.text
       email = self.ids.email.text
       passwd = self.ids.passwd.text
       passwd_confirm = self.ids.passwd_confirm.text


       #check if password matches
       if passwd != passwd_confirm:
           self.ids.passwd.error = True #show red box
           self.ids.passwd_confirm.helper_text = "Passwords don't match."


       check_query = f"SELECT * FROM user where username = '{uname}'OR email = '{email}' "
       db = DatabaseManager(name = 'user_info.db')
       result = db.search(query = check_query)


       if len(result) > 0:
           self.ids.uname.error = True
           self.ids.uname.helper_text = "Username or email entered has been used already."
           return


       #check if the fields are not empty
       if len(passwd) * len(passwd_confirm) * len(uname) * len(email) != 0:
           hashed_passwd = encrypt_password(passwd)
           insert_query = f"""INSERT into user(username, email, password)
                           values('{uname}', '{email}', '{hashed_passwd}')"""
           db.run_save(query = insert_query)
           db.close()
           LoginScreen.current_user = uname
           self.parent.current = 'HomeScreen'
           print('User successfully signed up')
else:
   if len(passwd) == 0:
       self.ids.passwd.helper_text = "Fill out here"
   if len(passwd_confirm) == 0:
       self.ids.passwd_confirm.helper_text = "Fill out here"
   if len(uname) == 0:
       self.ids.uname.helper_text = "Fill out here"
   if len(email) == 0:
       self.ids.email.helper_text = "Fill out here"


```
Firstly, it takes all the inputs from the screen interacting with the kv file and stores them into the corresponding variables, `uname`, `email`, `passwd`, `passwd_confirm`. It checks if the password inputted the first time and the second time are equal to each other. If not, the password text field that is to confirm will be highlighted and helper text displays. This avoids users registering passwords that they did not intend. Then, `check_query` stores the SQL command to search from the `user` table from `user_info.db`. Using the function `DatabaseManager` that is developed to manage the database in the other file, the variable `result` stores every element from the `user` table where the username is equal to the username inputted, or email is equal to the email inputted. If so, it will display errors by showing a red box for the username text field, and ask users to input different strings. This ensures no errors when logging into their account or any potential security risks. Third, it checks if any of the text fields are not empty to ensure nothing is missing when registering. This is done by getting the length of `passwd`, `passwd_confirm`, `uname` and `email` and multiplying each other. If the result is not equal to 0, it indicates that none of the text fields are left empty. It uses the function imported, `encrypt_password`, to hash the password before inserting information into the database, `user`. By declaring the variable, `insert_query`, and store the SQL command that inserts new columns with the values of `uname`, `email`, and `hashed_passwd` into the corresponding columns in `user`. Using the pre-developed function `run_save(query)` from `DatabaseManager`, the command is executed and stores new user’s information into the database `user`. It closes the database to prevent corruption of the database. It navigates to HomeScreen. Lastly, by checking which inputs are empty, it highlights the text box wherever the text fields are empty as to indicate what is causing the registration to not be completed.

Firstly, I encountered a difficulty to deal with every possible errors, but by organizing it using if statements, I was successfully able to manage them developing to fulfill success criteria 1.

Success Criteria 3: Booking Manager System

## 4. **Function** / **Iteration** / **If Statements**
As per success criteria **[success criteria 5]**, the application needs to allow the user to book a table for a restaurant. To address this, I decided to create a function interacting with the kv file within the `BookingManagerScreen` which is only accessible to admin users. 
From `main.py`:
```python
def delete(self, instance):
   if self.selected_row:
       for row in self.selected_row:
           reservation_id = row[0][0]
           query = f"""DELETE FROM reservation where id = '{reservation_id}'"""
           db = DatabaseManager('user_info.db')
           delete = db.run_save(query)
       self.selected_row = []
       self.update()
       return
   else:
       self.ids.delete.helper_text = "Please click on the box to delete."
       return
```
First conditional statement checks if `self.selected_row` (which is a list, declared in another function within the same class. It stores data of all rows that checkbox is activated.). If yes, it will iterate through each element of the `self.selected_row`, and the variable name given for each row is `row`. Within the iteration, `reservation_id` is extracted from the index of 0 of the index of 0 in `row` since `row` is composed of a list within the list. The variable `query` stores the SQL command that deletes one row of reservation where the `id` column from `reservation` is equal to `reservation_id` declared before. Using `DatabaseManager`, the command is executed. After the iteration, the `self.selected_row` will be blank in order to prevent the program from trying to delete the reservation that does not exist or a different reservation from the one that is intended to delete. Lastly,  `self.update()` is called which refreshes the database as shown below. 
While the iteration is executed, in `else`, the MDButton that has the id of `delete`’s helper text is displayed saying “Please click on the box to delete.” to show the error message.

From `main.py`:
```python
def update(self):
   db = DatabaseManager('user_info.db')
   data = db.search("SELECT id, last_name, phone_num, reservation_time, reservation_date, seat_type from reservation") # the # of column = elements
   self.data_table.update_row_data(None, data)
   db.close()
```
It is created to update the table shown in the `BookingManagerScreen` to make it able to modify and update the table quickly allowing users to be more efficient rather than manually refreshing the table. 
It uses the `DatabaseManager` to open the database `user_info.db` and select columns of `id`, `last_name`, `phone_num`, `reservation_time`, `reservation_date`, and `seat_type` from the table named `reservation`. Then call the methods to refresh the table by taking `None` to take every row and `data` to replace the current data as arguments. Finally, it closes the datatable to prevent corruption. 


