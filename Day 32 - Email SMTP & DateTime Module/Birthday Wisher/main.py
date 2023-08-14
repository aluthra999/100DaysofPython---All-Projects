import smtplib

my_email = "pythonsmtpudemy@gmail.com"
app_password = "cjrxivkavqvbtqwn"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(
        user=my_email,
        password=app_password
    )
    connection.sendmail(
        from_addr=my_email,
        to_addrs="pythonsmtpudemy@yahoo.com",
        msg="Subject:Hello\n\nIs it Working?"
    )
