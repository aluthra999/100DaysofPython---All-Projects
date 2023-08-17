# ---- import libraries ---- #
import csv
import smtplib
from datetime import datetime
import random

MY_EMAIL = "YOUR@EMAIL.COM"
APP_PASSWORD = "YOUR_PASSWORD"

# Get today's date
today = datetime.now().date()

# 1. Update and open the birthdays.csv
with open('birthdays.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

# 2. Check if today matches a birthday in the birthdays.csv
    for row in csv_reader:
        birthday_date = datetime(int(row['year']), int(row['month']), int(row['day'])).date()
        if birthday_date.month == today.month and birthday_date.day == today.day:
            person_name = row['name']
            person_email = row['email']
            # print(f"Today is {row['name']}'s birthday! Send them best wishes to {row['email']}.")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
letter_number = random.randint(1, 3)
with open(f'letter_templates/letter_{letter_number}.txt', 'r') as template_file:
    letter_content = template_file.read()

    # Replace [NAME] with the person's name
    letter_content = letter_content.replace('[NAME]', person_name)
    letter_content = letter_content.replace('[YOUR_NAME]', 'YOUR NAME')

    # Print the modified letter
    # print(letter_content)

# 4. Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(
        user=MY_EMAIL,
        password=APP_PASSWORD
    )
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=person_email,
        msg=f"Subject:Happy Birthday\n\n{letter_content}"
    )
