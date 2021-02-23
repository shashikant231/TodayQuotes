import csv
import random
import datetime as dt
import smtplib

with open("quotes.txt","r") as new_file:
    all_quotes = new_file.readlines()




        
my_email = "youremail@gmail.com"
password = "yourpassword"

now = dt.datetime.now()
weekday  = now.weekday()
#if today is monday
if weekday == 0:
    x = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr=my_email ,
            to_addrs= my_email ,
            msg = "subject:Today Quotes \n\n Good Morning \n{}".format(x)
         )
