import random
import pandas
import smtplib
import datetime

def send_email():
    my_email = "@gmail.com"
    password = ""
    with smtplib.SMTP("smtp.gmail.com") as mail:
        mail.starttls()  # encrypt the email during transfer
        mail.login(user=my_email, password=password)
        mail.sendmail(
            from_addr=my_email,
            to_addrs=bday_person.email,
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )



today = (datetime.datetime.now().month, datetime.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
print(data.to_dict())

new_data = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in new_data:
    bday_person = new_data[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as f:
        contents = f.read()
        contents.replace("[NAME]", bday_person["name"])
    send_email()