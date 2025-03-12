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

## Citation
[^1]: **"Should You Use CSV, JSON, or SQL?"** *PythonHow*. [https://pythonhow.com/python-tutorial/miscellaneous/csv-json-or-sql/](https://pythonhow.com/python-tutorial/miscellaneous/csv-json-or-sql/).  
[^2]: Nelson, Carter. **“Modern Replacements for DHT11 and DHT22 Sensors.”** *Adafruit Learning System*. [https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives](https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives).  
[^3]: Gomez, Jose. **“Web Apps Vs. Desktop Apps: Understanding the Differences.”** *Koombea*, 16 Nov. 2023. [https://www.koombea.com/blog/web-apps-vs-desktop-apps/](https://www.koombea.com/blog/web-apps-vs-desktop-apps/). Accessed 10 Mar. 2024.  
[^4]: Juviler, Jamie. **“What Is GUI? Graphical User Interfaces, Explained.”** *HubSpot Blog*, 30 Aug. 2023. [https://blog.hubspot.com/website/what-is-gui](https://blog.hubspot.com/website/what-is-gui). Accessed 10 Mar. 2024.  
[^5]: Tino. **Tino/PyFirmata: Python Interface for the Firmata Protocol.** *GitHub*. [https://github.com/tino/pyFirmata](https://github.com/tino/pyFirmata). Accessed 10 Mar. 2024.  
[^6]: **"Advantages of Python: Disadvantages of Python."** *Python Geeks*, 26 June 2021. [https://pythongeeks.org/advantages-disadvantages-of-python/](https://pythongeeks.org/advantages-disadvantages-of-python/).  
[^7]: **"Python vs C++: Selecting the Right Tool for the Job."** *Real Python*, 19 June 2021. [https://realpython.com/python-vs-cpp/#memory-management](https://realpython.com/python-vs-cpp/#memory-management).  
