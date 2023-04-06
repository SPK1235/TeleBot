import json
import requests as req


def weather(cod_loc):
    token_accu = 'nkmyWPCklLNaekX8wHc4EpEvJWfuvPrg'
    #url_weather = f'http://dataservice.accuweather.com/locations/search.json?q={latitude},{longitude}&apikey={token_accu}'
    url_weather = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{cod_loc}?apikey={token_accu}&language=ru&metric=True'
    response = req.get(url_weather, headers={"APIKey": token_accu})
    print(response.text)
    print(response.status_code)
    """json_data = json.loads(response.text)
    dict_weather = dict()
    dict_weather['link'] = json_data[0]['MobileLink']
    dict_weather['сейчас'] = {'temp': json_data[0]['Temperature']['Value'], 'sky': json_data[0]['IconPhrase']}
    for i in range(len(json_data)):
        time = 'через' + str(i) + 'ч'
        dict_weather[time] = {'temp': json_data[i]['Temperature']['Value'], 'sky': json_data[i]['IconPhrase']}
    return dict_weather"""


def code_location(latitude: str, longitude: str, token_accu: str):
    url_location_key = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={token_accu}&q={latitude},{longitude}&language=ru'
    resp_loc = req.get(url_location_key, headers={"APIKey": token_accu})
    json_data = json.loads(resp_loc.text)
    code = json_data['Key']
    return code


latitude = '55.768425'
longitude = '36.986632'
token_accu = 'nkmyWPCklLNaekX8wHc4EpEvJWfuvPrg'
cod_loc = code_location(latitude, longitude, token_accu)
print(cod_loc)
print(weather(cod_loc))