import openpyxl
from datetime import datetime

class Excel:

    def __init__(self):
       self.wb = openpyxl.load_workbook('cities.xlsx')
       self.worksheet = self.wb['Tabelle1']
       self.cells = [
           {'city': 'Moscow',
           'c': 'C3',
           'f': 'D3'},
           {'city': 'Berlin',
           'c': 'C4',
           'f': 'D4'},
           {'city': 'London',
           'c': 'C5',
           'f': 'D5'},
           {'city': 'Saint Petersburg',
           'c': 'C6',
           'f': 'D6'},
           {'city': 'Dresden',
           'c': 'C7',
           'f': 'D7'},
       ]
    
    def write(self, weather_cities):
        for city in weather_cities:
            for cell in self.cells:
                if cell['city'] == city['city']:
                    self.worksheet[cell['c']] = city['celsius']
                    self.worksheet[cell['f']] = city['fahrenheit']

    def save_file(self):
        self.wb.save('cities_{}_{}.xlsx'.format(datetime.strftime(datetime.now(), "%Y.%m.%d"), datetime.strftime(datetime.now(), "%H.%M.%S")))
 