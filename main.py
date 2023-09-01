from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "bcamp112233@gmail.com"
MY_PASSWORD = "cfzsuvmposgohpfv"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {()}
