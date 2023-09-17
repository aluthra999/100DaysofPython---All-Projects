import smtplib

SENDER_EMAIL = ""
APP_PASSWORD = ""
RECEIVER_EMAIL = ""


class Mail:
    def __init__(self, headline, link):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject:Today's Update\n\n"
                    f"{headline}"
                    f"{link}"
            )
