import datetime
import datetime as dt
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager


# ------------------CONSTANTS---------------------- #
DAY_IN_ADVANCE = 180
FROM_AIRPORT_IATA = "FRA"


# Setup Objects from the classes
trip_search = FlightSearch()
sheety = DataManager()
twilio = NotificationManager()

## TODO complete the IATA of the Spreadsheet.
# get "city" data from the spreadsheet with sheety
# pass it to the location api of kiwi. get the IATA code.
# Write the iata code to the sheet with sheety.
# iata_code_list = [trip_search.search_term(city) for city in sheety.cities]

#for i in range(len(iata_code_list)):
#     sheety.table[i]['iataCode'] = iata_code_list[i]

print(sheety.table)
x = 2

# -----UNCOMMENT THOSE 4 LINES TO ADD IATA CODES OF THE AIRPORT TO THE SHEET------- #
# writes the sheety.table as "put" to the spreadssheet. Adds the iata in that way
# for entry in sheety.table:
#    sheety.put_table(row=x, iata=entry["iataCode"])
#   x+=1

## TODO complete the prices in the Spreadsheet.
# get the IATA code from sheety. Search the cheapest price within the next 6 months
# update the sheet prices
now = dt.datetime.now()

in_six_month = now + datetime.timedelta(days=DAY_IN_ADVANCE)

trip_search.get_data(iata_from=FROM_AIRPORT_IATA, iata_to="LAS", date_from=now.strftime("%d/%m/%Y"),
                                date_to=in_six_month.strftime("%d/%m/%Y"))
print(trip_search.cheapest_price)
print(trip_search.cheapest_flight_dict)
y=1
for entry in sheety.table:
    y+=1
    try:
        trip_search.get_data(iata_from=FROM_AIRPORT_IATA, iata_to=entry["iataCode"], date_from=now.strftime("%d/%m/%Y"),
                             date_to=in_six_month.strftime("%d/%m/%Y"))
    except IndexError:
        try:
            print("hello")
            trip_search.max_stopovers = 1
            trip_search.get_data(iata_from=FROM_AIRPORT_IATA, iata_to=entry["iataCode"], date_from=now.strftime("%d/%m/%Y"),
                             date_to=in_six_month.strftime("%d/%m/%Y"))
            trip_search.max_stopovers = 0
        except IndexError:
            continue
        else:
            if trip_search.cheapest_price < int(entry["price"]):
                sheety.put_new_price(trip_search.cheapest_price, row=y)
                twilio.send_notification_with_stopover(trip_search.cheapest_flight_dict, sheety.subscribers)


    else:
        print(f"Frankfurt to {entry['city']} and back: {trip_search.cheapest_price}")
        if trip_search.cheapest_price < int(entry["price"]):
            sheety.put_new_price(trip_search.cheapest_price, row=y)
            twilio.send_notification(trip_search.cheapest_flight_dict, sheety.subscribers)






