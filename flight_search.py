import requests


class FlightSearch:
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.endpoint_location = "https://tequila-api.kiwi.com/locations/query"
        self.endpoint_nomad = "https://tequila-api.kiwi.com/v2/nomad"
        self.response = {}
        self.cheapest_flight_dict = {}
        self.cheapest_price = 0
        self.header = {"apikey": "[API-KEY]"}
        self.search_response = {}
        # sets the minimum and maximum length of stay
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 25
        # sets the maximum hours of flying
        self.max_stopovers = 0



# Please insert date_from and date_to in the format "02/04/2022"
    def get_data(self, iata_from, iata_to, date_from, date_to):
        self.body_query = {
            "fly_from": f"city:{iata_from}",
            "fly_to": iata_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": self.nights_in_dst_to,
            "nights_in_dst_to": self.nights_in_dst_to,
            "flight_type": "round",
            "adults": 1,
            "max_stopovers": self.max_stopovers,
            "one_for_city": 1
        }
        self.response = requests.get(url=self.endpoint, params=self.body_query, headers=self.header)
        self.response.raise_for_status()
        # self.cheapest_flight_dict = self.response.json()["data"][0]
        # self.cheapest_price = self.response.json()["data"][0]["price"]
        self.cheapest_price = self.response.json()["data"][0]["price"]
        self.cheapest_flight_dict = self.response.json()["data"][0]

# returns the IATA Code of the main airport of the city which is entered as "term"
    def search_term(self, term:str):
        self.body_term ={"term": term, "limit": 1}
        self.search_response = requests.get(url=self.endpoint_location, headers=self.header, params=self.body_term)
        self.search_response.raise_for_status()
        return self.search_response.json()["locations"][0]["code"]
