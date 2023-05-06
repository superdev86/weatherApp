import requests
import datetime

api_key = "fac026fb3da0cf0e4ebcf71ad19b3375" 
url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}"
city = str(input("Which city would you like me to check the weather for?\n")).capitalize()
data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()

#ends program if status code is not correct
if (data["cod"] != 200):
    print("Invalid city")
else:
    #weather forecast 
    weather = data["weather"][0]["description"]

    #convert kelvin to fahrenheit and celsius
    kelvin = data["main"]["temp"]

    def get_fahrenheit(kelvin):
        fahr = (kelvin - 273.15) * (9/5) + 32
        return fahr
    
    def get_celsius(kelvin):
        cels = kelvin - 273.15
        return cels

    #lowest and highest temp
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]

    #feels like temp
    feels_like = data["main"]["feels_like"]

    #humidity %
    humidity = data["main"]["humidity"]

    #sunrise and sunset times
    sunrise_time = datetime.datetime.utcfromtimestamp(data["sys"]["sunrise"])
    sunset_time = datetime.datetime.utcfromtimestamp(data["sys"]["sunset"])

    print(f"{city} Forecast")
    print("---------------------")
    print(f"Weather in {city} is {weather}")
    print(f"Temperature in {city} is {get_fahrenheit(kelvin):.2f}°F or {get_celsius(kelvin):.2f}°C")
    print(f"Today's temperature in {city} will have a high of {get_fahrenheit(temp_max):.2f}°F/{get_celsius(temp_max):.2f}°C"
          f" and a low of {get_fahrenheit(temp_min):.2f}°F/{get_celsius(temp_min):.2f}°C")
    print(f"{city} feels like {get_fahrenheit(feels_like):.2f}°F or {get_celsius(feels_like):.2f}°C")
    print(f"The humidity in {city} is {humidity}%")
    print(f"The sunrise in {city} is at {sunrise_time}")
    print(f"The sunset in {city} is at {sunset_time}")