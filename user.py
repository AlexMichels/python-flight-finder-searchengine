from data_manager import DataManager

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email_name = input("What is your email?\n")

sheety = DataManager()
sheety.add_subscriber(email=email_name,first_name=first_name,last_name=last_name)