from weather import Weather
from excel import Excel
from notepad import Notepad

cities = ['Moscow', 'Berlin', 'London', 'Saint Petersburg', 'Dresden']

weather = Weather()

cities_weather = []
for city in cities:
    celsius = weather.get_weather(city)

    cities_weather.append({
        'city': city,
        'celsius': celsius,
        'fahrenheit': round((celsius*9/5)+32)})

weather.close_window()

excel = Excel()
excel.write(cities_weather)
excel.save_file()

notepad = Notepad()
notepad.barmaglot()