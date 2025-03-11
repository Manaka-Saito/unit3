### have to be measureable
### use gy and good coding practices
### issue tackled should be there

## one small one medium one complexed for the flow chart
## list of techniques

### password hashing
### web sessions
### sql trigger with complex sql methods

[![image](https://github.com/user-attachments/assets/a24f3bcd-d713-40ba-b350-8bb862083b09)
](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.lacademie.com%2Fnepalese-food-guide%2F&psig=AOvVaw3PdlZaKWTHtL134Ew3Xs1D&ust=1739447146860000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPiKkdyHvosDFQAAAAAdAAAAABAR)

# Unit 3: A Restaurant Manager

## Criteria A: Planning

## Problem definition

My client, T.L., recently opened a local restaurant, Tenzin’s Food, which serves Nepalese food. He is currently advertising his restaurant by putting up posters in local newspapers and distributing them to local people. Additionally, he manages employees and customer information manually resulting in inefficiency in operations. Finally, he takes orders for take away and reservations on call and records manually. He is willing to expand his business and  get more foreign customers or customers from outside of the community. 

## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. I considered alternatives such diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python's open-source nature and platform independence contribute to the long-term viability of the system. The use of Python simplifies potential future enhancements or modifications, allowing for seamless scalability without the need for extensive redevelopment [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.  


## Success Criteria

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 

1. The solution provides a visual representation of the Humidity, Temperature and atmospheric pressure (HL) values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. ```** [Issue tacled] **: fill in here```
1. ```[HL]``` The local variables will be measure using a set of sensors around the dormitory.```** [Issue tacled] **: fill in here```
2. The solution provides a mathematical modelling for the Humidity, Temperature and atmospheric pressure (HL) levels for each Local and Remote locations. ```(SL: linear model)```, ```(HL: non-lineal model)``` ```** [Issue tacled] **: fill in here```
3. The solution provides a comparative analysis for the Humidity, Temperature and atmospheric pressure (HL) levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median. ```** [Issue tacled] **: fill in here```
4. ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server as a backup. ```** [Issue tacled] **: fill in here```
5. The solution provides a prediction for the subsequent 12 hours for Humidity, Temperature and atmospheric pressure (HL). ```** [Issue tacled] **: fill in here```
6. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Humidity, Temperature and atmospheric pressure (HL). ```** [Issue tacled] **: fill in here```

_TOK Connection: To what extent does ```the use of data science``` in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the ```reliability, interpretation, and ethical implications``` of data-driven approaches in addressing climate change_

1. How does our use of technology shape our understanding of the environment
2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?
3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus? 

# Criteria B: Design

## System Diagram
<img width="max" alt="Screenshot 2025-03-11 at 22 52 11" src="https://github.com/user-attachments/assets/4ab179c7-bb5a-4d63-9358-a36a24febf5f" />

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
| 21.  | MVP     | Recieve feedback from clients, knowing where to fix to finalize the application.                                                                                                                                                                                                                                                              | 30                  | Mar. 7                 | A         |
| 22.  | Finalize the Application     | Reflecting on the feedback gained from MVP, finalize the application by adjusting the application.                                                                                                                                                                                                                                            | 60                  | Mar. 8                 | C         |
| 23.  | Documentation     | Complete the project documentation by writing about the planning, design, development, and functionality. Also, record a video to explain these aspects.                                                                                                                                                                                      | 180                 | Mar. 11                | A/B/C/D   |
## Test Plan


# Criteria C: Development (around 1000 word max)

## List of techniques used

1. 
2. 
3. 

### 1. Filtering using moving average

Things to explain: a) what problem are you trying to solve (what success criteria), b) demonstrate your technical
understanding, c) algorithmic thinking.

Ex: To solve SC#1 I encounter the problem that the values from teh sensors are noisy due to the changes in the
temperature and other variables. I thougt about using an algorithm to filter the data and smooth it. After some reseach
I decided to use the moving average. To make things more sustainable and organized I decided to use a function to
implemented the moving average and placed it in a library.
```.py
def moving_average(windowSize:int, x:list)->list:
    # this function  has a purpose XXXX
    #The inputs are XXXXX
    # the output is xxxx
    x_smoothed = []
    for i in range(0, len(x)-windowSize):
        x_section = x[i:i+windowSize]
        x_average = sum(x_section)/windowSize
        x_smoothed += [x_average]

    return x_smoothed
```
In the code above, we can see that the function signature includes two inputs, ```windowSize:int ``` is the size used for filtering which is of
data type integer.....


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
