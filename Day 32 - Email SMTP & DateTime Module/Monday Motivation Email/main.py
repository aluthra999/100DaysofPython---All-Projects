import smtplib
import datetime as dt
import random


# ------------- Generate Email Text ---------------- #
# Read the contents of the text file
with open('quotes.txt', 'r') as file:
    quotes = file.readlines()

# Remove any leading/trailing whitespace from each quote
quotes = [quote.strip() for quote in quotes]

# Pick a random quote from the list
random_quote = random.choice(quotes)

# ------------- Find The Day of Week ---------------- #
# Get the current date
current_date = dt.datetime.now()

# Check if the current day is Monday (0 corresponds to Monday)
if current_date.weekday() == 1:
    # ------------- Send Email ---------------- #
    my_email = "YOUR_EMAIL@gmail.com"
    app_password = "YOUR_APP_PASSWORD"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(
            user=my_email,
            password=app_password
        )
        connection.sendmail(
            from_addr=my_email,
            to_addrs="RECIPIENT@EMAIL.COM",
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
        )
