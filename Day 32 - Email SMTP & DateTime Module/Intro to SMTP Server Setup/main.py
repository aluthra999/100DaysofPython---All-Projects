import smtplib

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
        msg="Subject:SUBJECT\n\nBODY TEXT GOES HERE!?"
    )
