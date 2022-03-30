import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    # Add your API Key here
    def __init__(self):
        self.endpoint = "https://api.sheety.co/[API-KEY]/flightDeals/prices"
        self.header = {"Authorization": "Bearer blablablathisisablatooken"}
        self.table = self.get_table()
        self.subscribers = self.get_subs()
        self.cities = [entry["city"] for entry in self.table]
        self.iata = [entry["iataCode"] for entry in self.table]
        self.price = [entry["price"] for entry in self.table]



    # gets the spreadssheet data with "get"
    def get_table(self):
        self.response = requests.get(url=self.endpoint, headers=self.header)
        self.response.raise_for_status()
        return self.response.json()["prices"]

    def get_subs(self):
        response = requests.get(url="https://api.sheety.co/[API-KEY]/flightDeals/users",
                                headers=self.header)
        response.raise_for_status()
        return response.json()["users"]
   # changes the existing table with the put request
    def put_table(self, iata:str, row:int):
        self.put_request = requests.put(url=f"https://api.sheety.co/[API-KEY]/flightDeals/prices/{str(row)}", json={"price": {"iataCode": iata}}, headers=self.header)
        self.put_request.raise_for_status()
        print(self.put_request)

    # takes a list of new prices and insert it to the sheety

   # insert the new price
    def put_new_price(self, price:str, row:int):
        self.put_request = requests.put(url=f"https://api.sheety.co/[API-KEY]/flightDeals/prices/{str(row)}", json={"price": {"price": price}}, headers=self.header)
        self.put_request.raise_for_status()
        print(self.put_request)

    # add subscriber
    def add_subscriber(self, email, first_name, last_name):
        body = {"user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }}
        response = requests.post(url="https://api.sheety.co/[API-KEY]/flightDeals/users",
                                 json=body, headers=self.header)
        response.raise_for_status()
        print(response)
