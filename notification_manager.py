from twilio.rest import Client
import smtplib


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "[API-KEY]0"
        self.auth_token = "[API-KEY]8"


    def send_notification(self,flightdata:dict, subs_sheet):
        client = Client(self.account_sid, self.auth_token)
        text_message= f"Low price alert! Only {flightdata['price']}€ to fly from " \
                 f"{flightdata['cityFrom']}-{flightdata['flyFrom']} to {flightdata['cityTo']}" \
                      f"-{flightdata['cityCodeTo']}, from {flightdata['route'][0]['local_departure'].split('T')[0]}" \
                      f" to {flightdata['route'][1]['local_departure'].split('T')[0]} "
        message = client.messages \
            .create(
            body= text_message,
            from_="+17655713110",
            to="+4915162505755")
        print(flightdata)
        my_email = "pythonfuture1@gmail.com"
        with smtplib.SMTP("smtp.gmail.com:587") as connection:
            connection.starttls()
            connection.login(user=my_email, password="Nokia1993!")
            for entry in subs_sheet:
                connection.sendmail(from_addr=my_email, to_addrs=entry["email"],
                                    msg=f"Subject:Price Alert \n\n{flightdata['cityFrom']}-{flightdata['flyFrom']} to {flightdata['cityTo']}" \
                                        f"-{flightdata['cityCodeTo']}, from {flightdata['route'][0]['local_departure'].split('T')[0]}" \
                                        f" to {flightdata['route'][1]['local_departure'].split('T')[0]} ")

    def send_notification_with_stopover(self,flightdata:dict, subs_sheet):
        client = Client(self.account_sid, self.auth_token)
        text_message= f"Low price alert! Only {flightdata['price']}€ to fly from " \
                 f"{flightdata['cityFrom']}-{flightdata['flyFrom']} to {flightdata['cityTo']}" \
                      f"-{flightdata['cityCodeTo']}, from {flightdata['route'][0]['local_departure'].split('T')[0]}" \
                      f" to {flightdata['route'][1]['local_departure'].split('T')[0]} But you will have one stopover!"
        message = client.messages \
            .create(
            body= text_message,
            from_="+17655713110",
            to="+4915162505755")
        print(flightdata)
        my_email = "email"
        with smtplib.SMTP("smtp.gmail.com:587") as connection:
            connection.starttls()
            connection.login(user=my_email, password="password")
            for entry in subs_sheet:
                connection.sendmail(from_addr=my_email, to_addrs=entry["email"],
                                    msg=f"Subject:Price Alert \n\n{flightdata['cityFrom']}-{flightdata['flyFrom']} to {flightdata['cityTo']}" \
                      f"-{flightdata['cityCodeTo']}, from {flightdata['route'][0]['local_departure'].split('T')[0]}" \
                      f" to {flightdata['route'][1]['local_departure'].split('T')[0]} But you will have one stopover!")
