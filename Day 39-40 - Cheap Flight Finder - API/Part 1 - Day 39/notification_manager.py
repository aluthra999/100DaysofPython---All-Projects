import smtplib

APP_PASSWORD = "YOUR-APP-PASSWORD"
SENDER_EMAIL =  "YOUR-EMAIL"
RECEIVER_EMAIL = "RECEIVER-EMAIL"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(
                user=SENDER_EMAIL,
                password=APP_PASSWORD
            )
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject:Price Drop Alert\n\n{message}"
            )
