#######################################################################################
# FirstName/Surname:
# Student ID:
# Github repository URL: 
#######################################################################################
# Instruction
# Reads README.md in https://github.com/chotipat/NPA2023-Final-Example for more information.
#######################################################################################
 
#######################################################################################
# 1. Import libraries for API requests, JSON formatting, and time.

import requests  # Library for making HTTP requests
import json      # Library for working with JSON data
import time      # Library for time-related functions
from sent_message import sent_message

#######################################################################################
# 2. Assign the Webex hard-coded access token to the variable accessToken.


accessToken = "MDYwZmM5ZDMtYmZjYy00MWVkLTg1NDAtYzk2MjU3ZDUxY2IyOTMwYmE3NWYtMDYy_P0A1_7e57d048-2511-4d53-8dd4-05fe61659f5d" 

#######################################################################################
# 3. Prepare GetParameters to get the latest message for messages API.

# Defines a variable that will hold the roomId 
roomIdToGetMessages = "Y2lzY29zcGFyazovL3VzL1JPT00vZjBkZjY0NDAtYWU5Yi0xMWVlLTg5MGMtMGQzNjUwOTJlMmUy" 

while True:
    # always add 1 second of delay to the loop to not go over a rate limit of API calls
    time.sleep(1)

    # the Webex Teams GET parameters
    #  "roomId" is the ID of the selected room
    #  "max": 1  limits to get only the very last message in the room
    GetParameters = {
                            "roomId": roomIdToGetMessages,
                            "max": 1
                        }

#######################################################################################
# 4. Provide the URL to the Webex Teams messages API, and extract location from the received message.
    # Send a GET request to the Webex Teams messages API.
    # - Use the GetParameters to get only the latest message.
    # - Store the message in the "r" variable.
    r = requests.get("https://api.ciscospark.com/v1/messages",
                         params = GetParameters, 
                         headers = {"Authorization": f"Bearer {accessToken}"}
                    )
    # verify if the retuned HTTP status code is 200/OK
    if not r.status_code == 200:
        raise Exception( "Incorrect reply from Webex Teams API. Status code: {}. Text: {}".format(r.status_code, r.text))
    
    # get the JSON formatted returned data
    json_data = r.json()
    # check if there are any messages in the "items" array
    if len(json_data["items"]) == 0:
        raise Exception("There are no messages in the room.")
    
    # store the array of messages
    messages = json_data["items"]
    # store the text of the first message in the array
    message = messages[0]["text"]
    print("Received message: " + message)
    
    # check if the text of the message starts with the magic character "/" and yourname followed by a location name
    # e.g.  "/chotipat San Jose"
    if message.find("/") == 0:
        # extract name of a location (city) where we check for GPS coordinates using the OpenWeather Geocoding API
        # Enter code below to hold city name in location variable.
        # For example location should be "San Jose" if the message is "/chotipat San Jose".
        Name = message[1:message.find(" ")]
        location = message.split(" ", 1)[1]

#######################################################################################     
# 5. Prepare openweather Geocoding APIGetParameters..
        # Openweather Geocoding API GET parameters:
        # - "q" is the the location to lookup
        # - "limit" is always 1
        # - "key" is the openweather API key, https://home.openweathermap.org/api_keys
        openweatherGeoAPIGetParameters = {
            "q": location,
            "limit": 1,
            "appid": "eb84a3bb03a361e8c9ae42914ec98ac3",
        }

#######################################################################################       
# 6. Provide the URL to the OpenWeather Geocoding address API.
        # Get location information using the OpenWeather Geocoding API geocode service using the HTTP GET method
        r = requests.get("http://api.openweathermap.org/geo/1.0/direct", 
                             params = openweatherGeoAPIGetParameters
                        )
        # Verify if the returned JSON data from the OpenWeather Geocoding API service are OK
        json_data = r.json()
        # check if the status key in the returned JSON data is "0"
        if not r.status_code == 200:
            responseMessage = "Dear {}\nI am sorry, I cannot found {}. Please type location in List of ISO 3166 country codes".format(Name, location)
            sent_message(accessToken, responseMessage, roomIdToGetMessages)
            raise Exception("Incorrect reply from OpenWeather Geocoding API. Status code: {}".format(r.status_code))

#######################################################################################
# 7. Provide the OpenWeather Geocoding key values for latitude and longitude.
        # Set the lat and lng key as retuned by the OpenWeather Geocoding API in variables
        locationLat = json_data[0]["lat"]
        locationLng = json_data[0]["lon"]

#######################################################################################
# 8. Prepare openweatherAPIGetParameters for OpenWeather API, https://openweathermap.org/api; current weather data for one location by geographic coordinates.
        # Use current weather data for one location by geographic coordinates API service in Openweathermap
        openweatherAPIGetParameters = {
                                "lat": locationLat,
                                "lon": locationLng,
                                "appid": "eb84a3bb03a361e8c9ae42914ec98ac3",
                            }

#######################################################################################
# 9. Provide the URL to the OpenWeather API; current weather data for one location.
        rw = requests.get("https://api.openweathermap.org/data/2.5/weather", 
                             params = openweatherAPIGetParameters
                        )
        json_data_weather = rw.json()

        if not "weather" in json_data_weather:
            responseMessage = "Dear {}\nI am sorry, I cannot found the weather in {}.".format(Name, location)
            sent_message(accessToken, responseMessage, roomIdToGetMessages)
            raise Exception("Incorrect reply from openweathermap API. Status code: {}. Text: {}".format(rw.status_code, rw.text))

#######################################################################################
# 10. Complete the code to get weather description and weather temperature
        weather_desc = json_data_weather["weather"][0]["description"]
        weather_temp = round((float(json_data_weather["main"]["temp"])- 273.15), 2)

#######################################################################################
# 11. Complete the code to format the response message.
        # Example responseMessage result: In Austin, Texas (latitude: 30.264979, longitute: -97.746598), the current weather is clear sky and the temperature is 12.61 degree celsius.
        responseMessage = "Dear {}\nIn {} (latitude: {}, longitute: {}),\nThe current weather is {} and the temperature is {} degree celsius.\n".format(Name, location, locationLat, locationLng, weather_desc, weather_temp)
        # print("Sending to Webex Teams: " + responseMessage)

#######################################################################################
# 12. Complete the code to post the message to the Webex Teams room.         
        # the Webex Teams HTTP headers, including the Authoriztion and Content-Type
        sent_message(accessToken, responseMessage, roomIdToGetMessages)
