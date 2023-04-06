import requests
from bs4 import BeautifulSoup


api_key = '8537d9ef6386cb97156fd47d832f479c'
latitude = '55.768425'
longitude = '36.986632'
url_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'
resp = requests.get(url_weather, headers={"APIKey": api_key})
print(resp.text)

api_key = 'QF5UuSa0ss8qbEOPCDwslqAMvSkpxORQ'
latitude = '55.768425'
longitude = '36.986632'
url_weather = f'http://dataservice.accuweather.com/alarms/v1/1day/_{api_key}'
resp = requests.get(url_weather, headers={"APIKey": api_key})
print(resp.text)

"""latitude, longitude= '55.606187', '37.623366' # москва
parser_yandex_weather(latitude, longitude)
latitude, longitude = '53.915581', '27.662505' # минск
parser_yandex_weather(latitude, longitude)
latitude, longitude= '52.020719', '26.744966' # осовая
parser_yandex_weather(latitude, longitude)"""
"""latitude = '55.606368', longitude = '37.623273' # москва
parser_yandex_weather(latitude, longitude)
latitude = '55.606368', longitude = '37.623273' # москва
parser_yandex_weather(latitude, longitude)
latitude = '55.606368', longitude = '37.623273' # москва
parser_yandex_weather(latitude, longitude)"""

