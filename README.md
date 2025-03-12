## Criteria A: Planning

## Problem definition

My client, T.L., recently opened a local restaurant named Tenzin’s Kitchen, in a town famous for sightseeing, that serves Nepalese food. Currently, he has three problems he is facing. 
First problem, he is advertising his restaurant by putting up posters in local newspapers and at the front of his restaurant. However, he finds this not impactful since it is only to be reached to local people but not tourists which the town attracts approximately 100 people per month. He is seeking a better way to promote his restaurant. 
Secondly, he struggles to organize the reservations as they record every booking on paper. As his restaurant is flourishing, it is getting difficult for him to manage all the reservations and cancellations. 
Third, at the moment, he manages both his employer information on paper which requires him to spend hours to manage his business. There are some people that already left the restaurant but are still in the list of employees, or new employees that are not being added to his list of employees which causes confusion when operating.
Lastly, he takes orders of reservations on call and records manually as he cannot afford money to employ more than 5 people. He is currently getting help from his wife, but as she is working for another job, he needs to find another way of managing reservations very soon. 

## Proposed Solution
I propose to build a GUI application to address the client’s problems considering the future users. GUI can be quickly and easily navigated[^4]. Additionally, it does not require an internet connection; therefore, whenever the user needs to use the product, they have the ability to do so[^3].  
For a software tool to use, I propose Python. Python is a programming language that provides open-source access, meaning it can be used by anyone as long as it is installed[^6]. It also allows for the long-term viability of the system. The use of Python simplifies potential future modifications rather than requiring the application to be rebuilt[^7].  
KivyMD will be used to create interactive, well-designed interfaces. SQLite is the preferred data storage option, as it allows for a single codebase and is supported on a vast range of platforms. Although there are other options such as CSV files, SQLite is lightweight and well-structured, making it a suitable choice for this project[^1]. By combining Python, KivyMD, and SQLite, the solution can function smoothly and provide sufficient applications for my client.  

## Success Criteria


1. The solution has a login and sign-up system for users and distinguishes if it is either a customer or admin.```** [Issue tacled] **: he manages both his employer and customer information on paper which requires him to spend hours to manage his business```
2. The solution allows customers to browse the menu and information of the restaurant.```** [Issue tacled] **: he is advertising his restaurant by putting up posters in local newspapers and at the front of his restaurant. However, he finds this not impactful since it is only to be reached to local people…```
3. The solution allows the users to make a reservation for the restaurant.```** [Issue tacled] **: he needs to find another way of managing reservations soon```
4. The solution allows users to add and delete the employee information when they are admin. ```** [Issue tacled] **: he manages both his employer and customer information on paper which requires him to spend hours to manage his business.```
5. The solution allows users to delete the booking when cancelation happens when they are admin. ```** [Issue tacled] **: he struggles to organize the reservations as they records every bookings on paper```

## Client Approval of Success Criteria

<img width="max" alt="D90E800F-8D54-49F8-A7D0-BEC269D779EE" src="https://github.com/user-attachments/assets/a3f1a254-cfc2-480b-ad8c-6e94bfb135d9" />
Fig1. *Client's approval for the success criteria*

## Citation
[^1]: "Should You Use CSV, JSON, or SQL?" PythonHow. [https://pythonhow.com/python-tutorial/miscellaneous/csv-json-or-sql/](https://pythonhow.com/python-tutorial/miscellaneous/csv-json-or-sql/).  
[^2]:“MySQL.” Mysql.com, 2024, www.mysql.com/. Accessed 4 Mar. 2024.
[^3]: Gomez, Jose. **“Web Apps Vs. Desktop Apps: Understanding the Differences.”** *Koombea*, 16 Nov. 2023. [https://www.koombea.com/blog/web-apps-vs-desktop-apps/](https://www.koombea.com/blog/web-apps-vs-desktop-apps/). Accessed 10 Mar. 2024.  
[^4]: Juviler, Jamie. **“What Is GUI? Graphical User Interfaces, Explained.”** *HubSpot Blog*, 30 Aug. 2023. [https://blog.hubspot.com/website/what-is-gui](https://blog.hubspot.com/website/what-is-gui). Accessed 10 Mar. 2024.  
[^5]: Tino. *Tino/PyFirmata: Python Interface for the Firmata Protocol.GitHub*. [https://github.com/tino/pyFirmata](https://github.com/tino/pyFirmata). Accessed 10 Mar. 2025.  
[^6]: "Advantages of Python: Disadvantages of Python." Python Geeks, 26 June 2021. [https://pythongeeks.org/advantages-disadvantages-of-python/](https://pythongeeks.org/advantages-disadvantages-of-python/).  
[^7]: "Python vs C++: Selecting the Right Tool for the Job." Real Python, 19 June 2021. [https://realpython.com/python-vs-cpp/#memory-management](https://realpython.com/python-vs-cpp/#memory-management).  


# Criteria B: Design


## System Diagram

<img width="max" alt="Screenshot 2025-03-11 at 22 52 11" src="https://github.com/user-attachments/assets/4ab179c7-bb5a-4d63-9358-a36a24febf5f" />

Fig 1. *System Diagram of proposed solution*

## UML Diagram

![IMG_1889](https://github.com/user-attachments/assets/ae63417a-0f97-4114-b36c-bf5024498bcf)
Fig 2. *UML Diagram of proposed solution*


## ER Diagram

![IMG_1890 2](https://github.com/user-attachments/assets/899884a4-148c-40e5-84d7-e97ceb59330b)
Fig 3. *ER Diagram of proposed solution*

## Flow Diagrams

<img width="Max" alt="Screenshot 2025-03-12 at 18 01 03" src="https://github.com/user-attachments/assets/1abe3ec1-d69a-40bd-92e6-115e6d00f8e1" />
Fig 4. *Flow chart of `delete` method from class `BookingManagerScreen`*

<img width="max" alt="Screenshot 2025-03-12 at 17 35 20" src="https://github.com/user-attachments/assets/e8aca7e1-2cfb-4336-b64c-9cdc5e2c85a1" />
Fig 5. *Flow chart of `try_login` method from class `LoginScreen`*


<img width="Max" alt="Screenshot 2025-03-12 at 19 16 37" src="https://github.com/user-attachments/assets/32b054bc-1103-403c-bfa2-d59c342e5e12" />
Fig 6. *Flow chart of `submit_booking` method from class `BookingScreen`*

## Record of Tasks

|      |      | Planned Outcome                                                                                                                                                                                                                                                                                                                               | Time Estimate (Min) | Target Completion Date | Criterion |
|------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|------------------------|-----------|
| 1.   | Meet with my client     | Consultant with my client to clearly understand the situation know their needs.                                                                                                                                                                                                                                                               | 15                  | Jan. 29                | A         |
| 2.   | Define a problem definition     | Write a problem definition to clarify the problems that needs to be solved.                                                                                                                                                                                                                                                                   | 15                  | Feb. 3                 | A         |
| 3.   | Create and propose success criteria     | List all the success criteria and review them with client, getting consensus on all of them.                                                                                                                                                                                                                                                  | 30                  | Feb. 5                 | A         |
| 4.   | Create ER diagram     | Construct the ED diagram to organize relationships identifying attributes and figure out the data needed.                                                                                                                                                                                                                                     | 60                  | Feb. 12                | B         |
| 5.   | Create UML diagram     | Construct the UML diagram to understand the use of classes and variables needed to structure the whole app.                                                                                                                                                                                                                                   | 60                  | Feb. 15                | B         |
| 6.   | Create a system diagram     | Construct the sysmtem diagram to visualize the structure and deployment of the final application                                                                                                                                                                                                                                              | 40                  | Feb. 16                | B         |
| 7.   | Create and connect basic screens     | Create blank screens for all planned screens in the application, and put them into a ScreenManager to organize the screens within an application                                                                                                                                                                                              | 40                  | Feb. 16                | C         |
| 8.   | Signup Screen     | Create a sign up screen and a database and functions that stores unique id, username, email, and password. Insert the information that gets input into the screen into the database. Using the function, hash the password to protect information.                                                                                                                 | 100                 | Feb. 18                | C         |
| 9.   | Login Screen     | Create a login functions and allow uses to login by inputting the correct username and password.                                                                                                                                                                                                                                              | 100                 | Feb. 20                | C         |
| 10.  | Home Screen      | Create a home screen that displays information at the top and four buttons at the bottom to allow users to go move to different screens by clicking.                                                                                                                                                                                          | 40                  | Feb. 20                | C         |
| 11.  | Menu Screen     | Create a menu screen that has three buttons users can click to see details of menu, Breakfast, Lunch, and Dinner. Also it has a four buttons at the bottom to move to different screens by clicking.                                                                                                                                          | 60                  | Feb. 21                | C         |
| 12.  | Breakfast Screen     | Create a breakfast screen that displays all breakfast menu including other informations. There is a back arrow at the buttom to move back to menu screen.                                                                                                                                                                                     | 40                  | Feb. 22                | C         |
| 13.  | Lunch Screen     | Create a lunch screen that displays all lunch menu including other informations. There is a back arrow at the buttom to move back to menu screen.                                                                                                                                                                                             | 20                  | Feb. 22                | C         |
| 14.  | Dinner Screen     | Create a dinner screen that displays all dinner menu including other informations. There is a back arrow at the buttom to move back to menu screen.                                                                                                                                                                                           | 20                  | Feb. 22                | C         |
| 15.  | Booking Screen     | Create a booking screen as well as functions that allow users to specify their number of parties, date and time. User should also input first name, last name, and telephone number. The information input are recorded in the datatable. It should display error if there is any double bookings or limitation on number of praties to book. | 120                 | Feb. 25                | C         |
| 16.  | Admin Screen     | Create a admin screen that is used only when the user is admin. It has three buttons that allows users to use navigation between screens and logout.                                                                                                                                                                                          | 50                  | Feb. 26                | C         |
| 17.  | Booking Manager Screen     | Create a screen that shows the table of record of bookings made by users. When user is admin, the screen should be available and should be able to delete part of database.                                                                                                                                                                   | 90                  | Feb. 29                | C         |
| 18.  | Employee Manager Screen     | Create a screen that shows the table of record of employees that contains id, full name, and contact. When the user is admin, it is accessible and should be able to add/delete the database to manage the employees.                                                                                                                         | 120                 | Mar. 2                 | C         |
| 19.  | Test Running     | Test by running the whole application to fix any errors, and know overview of the application.                                                                                                                                                                                                                                                | 60                  | Mar. 3                 | C         |
| 20.  | Adjust UI     | Make the application user-friendly by controlling the element such as color, positions, size, and inserting pictures.                                                                                                                                                                                                                         | 70                  | Mar. 5                 | C         |
| 21.  | MVP     | Recieve feedback from clients and my coworkers, knowing where to fix to finalize the application.                                                                                                                                                                                                                                                              | 30                  | Mar. 7                 | A         |
| 22.  | Finalize the Application     | Reflecting on the feedback gained from MVP, finalize the application by adjusting the application.                                                                                                                                                                                                                                            | 60                  | Mar. 8                 | C         |
| 23.  | Documentation     | Complete the project documentation by writing about the planning, design, development, and functionality. Also, record a video to explain these aspects.                                                                                                                                                                                      | 180                 | Mar. 11                | A/B/C/D   |


## Test Plan

|     | Test Type            | Test Content                                  | Input                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Expected Output                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----|----------------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | Unit Testing         | Sign up                                       | Run python file(main.py). 1. Attempt to register without any input into provided text fields. 2. Attempt to register by inputting "a" as username, " a@gmail.com " as email, enter "a" as password at the third column, enter "a" as password confirmation at the fourth column. 3. Attempt to register by inputting "Alice" as username, " alice@gmail " as email, enter "alicealice123" as password at third column, enter "alicealice123" as password confirmation at the fourth column.4. Attempt to register by inputting "Alice" as username, " alice@gmail.com " as email, enter "alicealice123" as password at third column, enter "alicealice12345" as password confirmation at the fourth column. 5. Attempt to register by inputting "Alice" as username, " alice@gmail.com " as email, enter "alicealice123" as password at third column, enter "alicealice123" as password confirmation at the fourth column. | 1. Text saying “Fill out here” shows in each text field where the user needs to fill out the information. 2. Text saying “Username or email entered has been used already” shows in the first column. 3. Email input column is highlighted as red, showing that the email column is causing an error. 4.Text saying “Passwords don’t match” shows in the last column is the input text box, “Re-enter your password”. 5.User is redirected to HomeScreen |
| 2.  | Unit Testing         | Login                                         | Run python file(main.py). Go to the Login screen by clicking on the Login at the bottom of the signup screen. 1. Attempt to login without any input into provided text fields. 2. Attempt to login inputting “manaka” as username and “ma” as password. 3. Attempt to login inputting “manaka” as username and “manaringo” as password.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1. The top text box is highlighted red. 2. The second text box is highlighted red. 3. User is redirected to Home Screen                                                                                                                                                                                                                                                                                                                                  |
| 3.  | Unit Testing         | Booking                                       | Run python file(main.py). Login by inputting "manaka" as a username and "manaringo" as a password. Go to the booking screen, and 1. Attempt clicking Submit without any input into provided fields. 2. Attempt clicking Submit by inputting "Manaka" as first name, "Saito" as last name, and "123" as phone number, "2 Guests" as guests number, "2025-4-10" as date, "10 AM" as time, "Table" as a seating type. 3. Input the same information for each text field and dropdowns. 4. Logout once and login against by inputting “alice” as a username and “alicealice123” as a password. Go to the booking screen, and attempt clicking submit by inputting “Alice” as first name, “Smith” as last name, “14 Guests” as guests number, “2025-4-10” as date, “10 AM” as time, “Counter” as a seating type.                                                                                                                | 1. Text saying “Please fill out the form” is shown. 2. Text saying “Thank you! A table has been booked!” is shown. 3. Text saying “You already have one reservation on 2025-4-10. Please only make one reservation on one date” 4. Text saying “Sorry. We are currently only available from 13 people” shown.                                                                                                                                            |
| 4.  | Intergration Testing | Booking and update see my reservation pop-ups | Run python file(main.py). Login by inputting “yuzuka” as a username and "arsyuzuka" as a password. Go to the booking screen, and 1. Click the “See my reservation” button. 2. Input “Yuzuka” as first name, “Sato” as last name, and “123321” as phone number, “5 Guests” as guest number,“2025-4-10” as date, “10 AM” as time, “Table” as a seating type. Then click the “See my reservation” button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1. Pop up displays in the screen. The title is Reservation List and text says "No reservations found". 2. Pop-up displays in the screen. The title is Reservation List and the text says "#1 Name: Yuzuka Sato Time: 10:00 AM Date: 2025-04-10 Seat: Table" shown.                                                                                                                                                                                       |
| 5.  | Unit Testing         | Book Database                                 | Run python file (main.py). Login by inputting “Tenzin Wangdue Lama” as a username, and “tenzinskitchen123” as a password. Go to the database screen, and select a checkbox on the left that is on the row of id numbers. Click the delete reservation button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Table embedded will be modified. The row that is being selected disappears and the table gets updated.                                                                                                                                                                                                                                                                                                                                                   |
| 6.  | Unit Testing         | Delete row in Employee Database               | Run python file(main.py), login by inputting the same information as test number 5, and click on the book database button. Then click on the third checkbox in the table shown where id is “2”. Click on the delete button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Table embedded will be modified. The row that is being selected by checkbox disappears and the table gets updated.                                                                                                                                                                                                                                                                                                                                       |
| 7.  | Integration Testing  | Save a new employee in Employee Database      | Run python file (main.oy), login by inputting the same information as test number 5, and go to book database screen. 1. Then click on the save button without writing any inputs in given text fields. 2. Input "Hirose Akito" in full name text field and "hiro@gmail.com" in email text field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1. Text fields are highlighted red. 2. Table of employee gets updated and a new row is added. Elements shown are the following; The column of id is 2, full name is "Hirose Akito", contact is "hiro@gmail.com".                                                                                                                                                                                                                                         |
| 8.  | Unit Testing         | Menu screen and breakfast/lunch/dinner screen | Run python file, login by inputting the "a" as a username and "a" as a password. 1. Click on the Morning button, and scroll down to the bottom, and click on the back arrow icon. 2. Click on the Lunch, and scroll down to the bottom and click on the back arrow icon. 3. Click on the dinner, and scroll down to the bottom and click on the back arrow icon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1. Screen should be changed to breakfast menu, and then return to the Menu Screen. 2. Screen should be changed to lunch menu, and then return to the Menu Screen. 3. Screen should be changed to dinner menu, and then return to the Menu Screen.                                                                                                                                                                                                        |
| 9.  | Unit Testing         | Logout                                        | Run python file, login by inputting the same information as text number 5, and click on a logout button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | The screen is redirected to the login screen with no text field filled.                                                                                                                                                                                                                                                                                                                                                                                  |

Criterion C: Developing
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

## Criterion D: Functionality

Please go to the link below to see the video:
https://drive.google.com/drive/folders/1a-oqSG8ELJpTm6a67OQ2j7qTi1DBYKwE?usp=sharing
