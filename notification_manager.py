from twilio.rest import Client
import requests
import smtplib

#TWILIO
account_sid = 'TWILIO ID'
auth_token = 'TWILIO TOKEN'

#GOOGLE SHEET
USER_ENDPOINT = "SHEETY APY"
RECIPIENTS = []

#MY_EMAIL INFO
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "PASSWORD"


class NotificationManager:

    def send_text(self, body_message):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=body_message,
            from_='INSERT SENDER NUMBER',
            to='INSERT RECIPIENT NUMBER',
        )
        print(message.status)

    def send_email(self, message):
        response = requests.get(url=USER_ENDPOINT)
        data = response.json()['users']
        for email in data:
             RECIPIENTS.append(email['email'])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=RECIPIENTS,
                                msg=message)


