```from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import SlideTransition
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.screen import MDScreen
from paramiko.util import parse_ssh_config

from ProjectUnit3.py_file.mylib import DatabaseManager
from protectPasswd import check_hash, encrypt_password

import sqlite3

current_user = ''

class SignUpScreen(MDScreen):
    def try_signup(self):
        uname = self.ids.uname.text
        email = self.ids.email.text
        passwd = self.ids.passwd.text
        passwd_confirm = self.ids.passwd_confirm.text
        print(uname, email, passwd, passwd_confirm)

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

    def to_login(self):
        self.parent.current = 'LoginScreen'

#-----------------------------------------------------------------------------------------------------------------------
class LoginScreen(MDScreen):
    current_user = None
    checkbox_active = BooleanProperty(False)

    def try_login(self):
        uname = self.ids.uname.text
        passwd = self.ids.passwd.text
        self.ids.uname.error = False
        self.ids.passwd.error = False

        if len(uname)*len(passwd) == 0:
            if len(uname) == 0:
                self.ids.uname.helper_text = "Fill out here"
                self.ids.uname.error = True
            if len(passwd) == 0:
                self.ids.passwd.helper_text = "Fill out here"
                self.ids.uname.error = True
            return

        check_query = f"SELECT * FROM user where username = '{uname}'"
        db = DatabaseManager(name = "user_info.db")
        result = db.search(query = check_query)
        db.close()

        check_query = f"SELECT * FROM employee where employee_name = {uname} and status = TRUE"
        db = DatabaseManager(name = 'user_info.db')
        result_admin = db.search(query = check_query)
        db.close()

        if uname == "Tenzin Wangdue Lama" and passwd == 'tenzinskitchen123':
            LoginScreen.current_user = uname
            self.ids.uname.text = ''
            self.ids.passwd.text = ''
            self.parent.current = 'AdminScreen'

        else:
            id, uname, email, pass_config = result[0]
            if check_hash(input_str=passwd, hash = pass_config):
                LoginScreen.current_user = uname
                self.parent.current = 'HomeScreen'
            else:
                self.ids.uname.error = True
                self.ids.uname.helper_text = "Username or Password is incorrect"

    def to_signup(self):
        self.parent.current = 'SignUpScreen'


#-----------------------------------------------------------------------------------------------------------------------
class HomeScreen(MDScreen):
    def morning_show(self):
        self.parent.current = "MorningMenu"

    def lunch_show(self):
        self.parent.current = 'LunchMenu'

    def dinner_show(self):
        self.parent.current = 'DinnerMenu'

    def to_home(self):
        self.parent.current = "HomeScreen"

    def to_menu(self):
        self.parent.current = "MenuScreen"

    def to_booking(self):
        self.parent.current = 'BookingScreen'

    def to_logout(self):
        LoginScreen.current_user = ''
        self.parent.current = "LoginScreen"


#-----------------------------------------------------------------------------------------------------------------------
class CustomerScreen(MDScreen):
    def to_book_data(self):
        self.parent.current = "BookingManagerScreen"

    def to_employee_data(self):
        self.parent.current = "EmployeeManagerScreen"

    def to_logout(self):
        self.parent.current = "LoginScreen"
#-----------------------------------------------------------------------------------------------------------------------
class MenuScreen(MDScreen):

    def morning_show(self):
        self.parent.current = "MorningMenu"

    def lunch_show(self):
        self.parent.current = 'LunchMenu'

    def dinner_show(self):
        self.parent.current = 'DinnerMenu'

    def to_home(self):
        self.parent.current = "HomeScreen"

    def to_menu(self):
        self.parent.current = "MenuScreen"

    def to_booking(self):
        self.parent.current = 'BookingScreen'

    def to_logout(self):
        LoginScreen.current_user = ''
        self.parent.current = "LoginScreen"

class MorningMenu(MDScreen):
    def go_back_menu(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = "MenuScreen"
        self.parent.transition = SlideTransition(direction = 'left')

class LunchMenu(MDScreen):
    def go_back_menu(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = "MenuScreen"
        self.parent.transition = SlideTransition(direction = 'left')

class DinnerMenu(MDScreen):
    def go_back_menu(self):
        self.parent.transition = SlideTransition(direction="right")
        self.parent.current = "MenuScreen"
        self.parent.transition = SlideTransition(direction = 'left')

#-----------------------------------------------------------------------------------------------------------------------
class BookingScreen(MDScreen):
    def on_pre_enter(self, *args):
        self.selected_item = 'Counter'
        self.guest_menu_items = [
            {"text": f"{i} Guests", "viewclass": "OneLineListItem",
             "on_release": lambda x=f"{i} Guests": self.set_guests(x)}
            for i in range(1, 16)
        ]
        self.guest_menu = MDDropdownMenu(
            id = "guest_menu",
            caller=self.ids.guests_button,
            items=self.guest_menu_items,
            width_mult=4
        )

        # Menu for Time
        self.time_menu_items = [
            {"text": f"{hour}:00 PM", "viewclass": "OneLineListItem",
             "on_release": lambda x=f"{hour}:00 AM": self.set_time(x)}
            for hour in range(9, 12)
        ]+[
            {
                "text": f"{hour}:00 PM", "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{hour}:00 PM": self.set_time(x)}
            for hour in range(15, 22)
        ]

        self.time_menu = MDDropdownMenu(
            id = "time_menu",
            caller=self.ids.time_button,
            items=self.time_menu_items,
            width_mult=4
        )
        # self.add_widget(self.guest_menu)
        # self.add_widget(self.time_menu)

        # Set Guest Number

    def set_guests(self, text_item):
        self.ids.guests_button.text = text_item
        self.guest_menu.dismiss()

        # Set Time

    def set_time(self, text_item):
        self.ids.time_button.text = text_item
        self.time_menu.dismiss()

        # Show Date Picker

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.set_date)
        date_dialog.open()


    def set_date(self, instance, value, date_range):
        self.ids.date_button.text = value.strftime('%Y-%m-%d')

    def segment_active(self, instance, segmented_item):
        self.selected_item = instance.current_active_segment.text

    def cancel_book(self):
        self.ids.guests_button.text = "Select Guests"
        self.ids.time_button.text = "Select Date"
        self.ids.date_button.text = "Select Time"
        self.ids.first_name.text = ""
        self.ids.last_name.text = ""
        self.ids.phone_number.text = ""

    def submit_booking(self):
        guest_num = self.ids.guests_button.text
        time = self.ids.time_button.text
        date = self.ids.date_button.text
        seat = self.selected_item
        first_name = self.ids.first_name.text
        last_name = self.ids.last_name.text
        phone_num = self.ids.phone_number.text

        #check if the form is filled out
        if (len(first_name)*len(last_name)*len(phone_num) == 0 or
            guest_num == "Select Guests" or time == "Select Time" or date == "Select Date"):
            self.ids.availability.text_color = (1, 0, 0, 1)
            self.ids.availability.text = "Please fill out the form."
            return
        #check if...
        #1. there is no double-booking ✅
        #2. enough available seat ✅
        #3. make sure the telephone num is actlly int ✅

        elif phone_num.isdigit() is False:
            self.ids.availability.text_color = (1, 0, 0, 1)
            self.ids.phone_number.helper_text = "Only numbers are allowed"
            self.ids.phone_number.error = True
            self.ids.phone_number.helper_text_mode = "on_error"
            self.ids.availability.text = 'Phone Number only takes numbers'
            return

        #form is filled out✅
        else:
            #get the number fo guests user try to reserve for
            guest_num = guest_num.strip(' ')[0]
            guest_num = int(guest_num)

            #1. no double-booking
            check_query = f"""SELECT reservation_date FROM reservation 
                            where username = '{LoginScreen.current_user}' AND reservation_date = '{date}'"""
            db = DatabaseManager(name = "user_info.db")
            result_double_booking =  db.search(query = check_query)
            db.close()

            #2. availability of seats
            check_query = f"""SELECT * FROM availability where date = '{date}' AND time like '{time}'"""
            db = DatabaseManager(name = "user_info.db")
            result_full = db.search(check_query)
            db.close()

            new_seat = result_full[0][3]
            new_seat = int(new_seat)
            new_seat -= guest_num
            print(new_seat)

            # Check if the query returned a result
            if not result_full:
                self.ids.availability.text_color = (1, 0, 0, 1)
                self.ids.availability.text = "No availability found for this date and time."
                db.close()
                return

            if len(result_double_booking)>=1:
                self.ids.availability.text_color = (1, 0, 0, 1)
                self.ids.availability.text = f"You already have one reservation on {date}.\nPlease only make one reservation on one date."
                return

            elif new_seat<0:
                num_party = guest_num+new_seat
                self.ids.availability.text_color = (1, 0, 0, 1)
                self.ids.availability.text = f"Sorry. We are currently only available from {num_party} people."
                return

            else: #and new_seat>=0
                insert_query = f"""INSERT INTO 
                reservation(username, first_name, last_name, phone_num, reservation_time, reservation_date, seat_type) 
                values('{LoginScreen.current_user}','{first_name}','{last_name}', '{phone_num}', '{time}', '{date}', '{seat}')"""
                self.ids.availability.text_color = (0, 1, 0, 1)
                self.ids.availability.text = f"A {seat} booked! Thank you!!"
                db = DatabaseManager(name = 'user_info.db')
                db.run_save(insert_query)
                db.close()

                db = DatabaseManager(name = 'user_info.db')
                print(new_seat)
                update_query = f"""UPDATE availability set seat = '{new_seat}' where date = '{date}' and time = '{time}'"""
                db.run_save(update_query)
                db.close()
                return

    def show_reservation_popup(self):
        count = 0
        check_query = f"""SELECT * FROM reservation where username = '{LoginScreen.current_user}'"""
        db = DatabaseManager(name = 'user_info.db')
        result = db.search(check_query)
        print(result)
        db.close()
        text = ''
        if not result:
            text = "No reservations found."

        else:
            for r in result:
                count += 1
                text += "\n".join([f"#{count}  Name: {r[2]} {r[3]} Time: {r[5]} Date: {r[6]} Seat: {r[7]}\n"])

        self.dialog = MDDialog(
            title = "Reservation List",
            type = "custom",
            text = text,
            buttons=[
                MDRaisedButton(
                    text = "Close",
                    on_release = lambda _: self.dialog.dismiss()
                )
            ]
        )
        self.dialog.open()


    def morning_show(self):
        self.parent.current = "MorningMenu"

    def lunch_show(self):
        self.parent.current = 'LunchMenu'

    def dinner_show(self):
        self.parent.current = 'DinnerMenu'

    def to_home(self):
        self.parent.current = "HomeScreen"

    def to_menu(self):
        self.parent.current = "MenuScreen"

    def to_booking(self):
        self.parent.current = 'BookingScreen'

    def to_logout(self):
        LoginScreen.current_user = ''
        self.parent.current = "LoginScreen"



#-----------------------------------------------------------------------------------------------------------------------
class BookingManagerScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_table = None
        self.selected_row = []

    def on_pre_enter(self, *args):
        column_names = [('id', 40), ('Last Name', 40),
                        ('Contact', 40), ("Reserved Time", 40), ("Reserved Date", 40), ("Seat Type", 40)]
        #from datatable
        self.data_table = MDDataTable(
            size_hint = (.8, .5),
            pos_hint = {'center_x': .5, 'top': 0.8},
            use_pagination = True,
            check = True,
            column_data = column_names
        )
        self.data_table.bind(on_check_press = self.checkbox_pressed)
        self.add_widget(self.data_table)
        self.update() #method that I will create

        # clear_filter_button = MDRaisedButton(
        #     text="Clear Filters",
        #     size_hint=(0.8, None),
        #     height="40dp",
        #     pos_hint={"center_x": 0.5, "top": 0.55},
        #     on_press=self.clear_filters
        # )

    def update(self):
        db = DatabaseManager('user_info.db')
        data = db.search("SELECT id, last_name, phone_num, reservation_time, reservation_date, seat_type from reservation") # the # of column = elements
        self.data_table.update_row_data(None, data)
        db.close()

    # def row_pressed(self, table, cell): #cell = one pressed
    #     print(cell.text)

    def checkbox_pressed(self, table, row_list):
        if row_list:
            self.selected_row = row_list
            print(f"Selected rows: {self.selected_row}")
        else:
            print("No rows selected")

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

    def open_sort_menu(self, instance):
        # Create a list of sorting options
        sort_options = [
            {'viewClass': 'OneLineListItem', 'text': 'By Last Name (Alphabetical Order)', 'on_release': lambda: self.sort_data('last_name')},
            {'viewClass': "OneLineListItem", 'text': "By Today", 'on_release': lambda: self.sort_data('today')},
            {'viewClass': 'OneLineListItem', 'text': 'By Time (Early to Late)','on_release': lambda: self.sort_data('time_early_to_late')},
            {'viewClass': 'OneLineListItem', 'text': 'By Time (Late to Early)', 'on_release': lambda: self.sort_data('time_late_to_early')},
        ]

        # Check if the menu is already created, if not, create a new one
        if self.menu is None:
            self.menu = MDDropdownMenu(
                caller=instance,  # Set the caller as the MDDropDownItem widget itself
                items=sort_options,
                width_mult=4,
            )

        # Open the dropdown menu
        self.menu.open()


    def to_book_data(self):
        self.parent.current = "BookingManagerScreen"

    def to_employee_data(self):
        self.parent.current = "EmployeeManagerScreen"

    def to_logout(self):
        self.parent.current = "LoginScreen"
#-----------------------------------------------------------------------------------------------------------------------
class AdminScreen(MDScreen):
    def to_book_data(self):
        self.parent.current = "BookingManagerScreen"

    def to_employee_data(self):
        self.parent.current = "EmployeeManagerScreen"

    def to_logout(self):
        self.parent.current = "LoginScreen"


class EmployeeManagerScreen(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_table = None
        self.selected_row = []

    def on_pre_enter(self, *args):
        column_names = [('id', 40), ('Full Name', 90), ('Contact', 90)]
        #from datatable
        self.data_table = MDDataTable(
            size_hint = (.8, .5),
            pos_hint = {'center_x': .5, 'top': 0.8},
            use_pagination = True,
            check = True,
            column_data = column_names
        )
        self.data_table.bind(on_check_press = self.checkbox_pressed)
        self.add_widget(self.data_table)
        self.update() #method that I will create

    def checkbox_pressed(self, table, row_list):
        if row_list:
            self.selected_row = row_list
            print(f"Selected rows: {self.selected_row}")
        else:
            print("No rows selected")

    def update(self):
        data = test.db.search("SELECT id, employee_name, email from employee") # the # of column = elements
        self.data_table.update_row_data(None, data)

    def save(self):
        new_name = self.ids.name.text
        new_email = self.ids.email.text

        if new_name and new_email:
            query = f"""INSERT INTO employee(employee_name, email, status) values('{new_name}', '{new_email}', 0)"""
            db = DatabaseManager('user_info.db')
            db.run_save(query)
            db.close()
            self.ids.name.text = ''
            self.ids.email.text = ''
        else:
            if len(new_name) == 0:
                self.ids.name.helper_text_mode = 'on_error'
            if len(new_email) == 0:
                self.ids.name.helper_text_mode = 'on_error'

    def delete(self, instance):
        if self.selected_row != []:
            for row in self.selected_row:
                employee_id = row[0][0]
                query = f"""DELETE FROM employee where id = '{employee_id}'"""
                db = DatabaseManager('user_info.db')
                delete = db.run_save(query)
            self.selected_row = []
            self.update()
            return
        else:
            self.ids.delete.helper_text = "Please click on the box to delete."
            return


    def to_book_data(self):
        self.parent.current = "BookingManagerScreen"

    def to_employee_data(self):
        self.parent.current = "EmployeeManagerScreen"

    def to_logout(self):
        self.parent.current = "LoginScreen"



#-----------------------------------------------------------------------------------------------------------------------

class main(MDApp):
    db = DatabaseManager('user_info.db')
    def build(self):
        pass


# Create a table
db = DatabaseManager('user_info.db')

table = """CREATE table if not exists user(
    id integer primary key,
    username text unique,
    email text unique,
    password varchar(256)
    )
    """

db.run_save(table)
db.close()

db = DatabaseManager('user_info.db')

table_employee = """CREATE TABLE if not exists employee(
    id integer primary key, 
    employee_name text unique,
    email text unique,
    status boolean,
    password varchar(256)
    )
    """

# db.run_save(table_employee)
# passwd = 'tenzinskitchen123'
# hashed_passwd = encrypt_password(passwd)
# insert_admin = f"""INSERT INTO employee( employee_name, email, status, password)
#                 VALUES('Tenzin Wangdue Lama', '2026.tenzin.wangdue.lama@uwcisak.jp', TRUE, '{hashed_passwd}')"""
# db.run_save(insert_admin)
# db.close()

db = DatabaseManager('user_info.db')

table_book = """CREATE TABLE if not exists reservation(
    id integer primary key,
    username text,
    first_name text,
    last_name text,
    phone_num integer,
    reservation_time text,
    reservation_date text,
    seat_type text
    )"""

db.run_save(table_book)
db.close()

db = DatabaseManager('user_info.db')

table_availability = """CREATE TABLE IF not exists availability(
    id integer primary key,
    date text,
    time text,
    seat integer
    )"""

db.run_save(table_availability)
db.close()

conn = sqlite3.connect('user_info.db')
cursor = conn.cursor()

# months = [3,4,5,6,7,8,9,10,11,12]
# days_per_month = {3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# hours_am = range(9,12)
# hours_pm = range(15, 22)
#
# for month in months:
#     for day in range(1, days_per_month[month] + 1):
#         date_str = f"2025-{month:02d}-{day:02d}"
#
#         for hour in hours_am:
#             time_str = f"{hour:02d}:00 AM"
#             query = "INSERT INTO availability(date, time, seat) values (?,?,?)"
#             cursor.execute(query,(date_str, time_str, 15))
#
#         for hour in hours_pm:
#             time_str = f"{hour:02d}:00 PM"
#             query = "INSERT INTO availability(date, time, seat) values(?,?,?)"
#             cursor.execute(query, (date_str, time_str, 15))

# Commit the changes and close the connection
conn.commit()
conn.close()

test = main()
test.run()

```
