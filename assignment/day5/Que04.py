"""Write a Python program that:
Imports the datetime module
Displays the current date and time
Prints the day of the week for the current date"""


import datetime as dt

cdt = dt.datetime.now()
print("Current Date and Time:\t", cdt)
dow = cdt.strftime("%A")
print("Day of the Week:", dow)