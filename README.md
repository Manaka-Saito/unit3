## have 5-6 success criteria
### have to be measureable
### use gy and good coding practices
### issue tackled should be there

## one small one medium one complexed for the flow chart
## list of techniques

### password hashing
### web sessions
### sql trigger with complex sql methods
### automatic email creations

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

## System Diagram **SL**

![System Diagrams unit 2](https://github.com/user-attachments/assets/719228e9-3e4b-4e92-89a1-4a5887e0c73d)

**Fig.1** System diagram for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with the sensor DHT11 locally on an Arduino and remotely with a raspberry Pi. The latter implements an API (192.162.4.61/readings) providing access to remotely sensed data via ISAK-S network.


![System Diagrams unit 2 (1)](https://github.com/user-attachments/assets/7ec53d20-7afa-4279-8ac2-b5798e38f4db)

**Fig.2** System diagram (HL) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally. A remote server provides and API for remote monitoring and storage via the ISAK-S network. 

![System Diagrams unit 2 (2)](https://github.com/user-attachments/assets/36775cba-6730-45d3-bccb-57b4d8a8179d)

**Fig.3** Fig. 3 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally on a Raspberry Pi. A remote server provides and API for remote monitoring and storage (192.162.6.142) via the ISAK-S network. A laptop for remote work is included.

## Record of Tasks
| Task No. | Planned Action                                      | Planned Outcome                                                                              | Time Estimate (Min) | Target Completion Date | Criterion |
|----------|-----------------------------------------------------|----------------------------------------------------------------------------------------------|---------------------|------------------------|-----------|
| 1.       | Meeting with my client                              | Consultant with my client to clearly understand the situation know their needs.              | 15                  | Jan. 29                | A         |
| 2.       | Define the problem definition                       | Write a problem definition to clarify the problems that needs to be solved.                  | 15                  | Feb. 3                 | A         |
| 3.       | Propose and finalize a success criteria with client | List all the success criteria and review them with client, getting consensus on all of them. | 30                  | Feb. 5                 | A         |
| 4.       |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |
|          |                                                     |                                                                                              |                     |                        |           |## Test Plan

# Criteria C: Development (around 1000 word max)

## List of techniques used

1. API communication with remote server
2. Filtering using moving average
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
