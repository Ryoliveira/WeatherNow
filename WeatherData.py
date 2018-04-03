import configparser
import requests

confg = configparser.ConfigParser()
confg.read('keys.ini')
API_KEY = confg.get('ApiKey', 'Key')


class WeatherData():
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def get_weather_data(self):
        r = requests.get('http://api.wunderground.com/api/{}/conditions/q/{}/{}.json'.format(API_KEY, self.state, self.city))
        response = r.json()
        if 'error' in response['response']:
            self.data = 0
        if 'results' in response['response']:
            print("More than one result")
            self.data = response['response']
        else:
            print(len(response))
            self.data = response["current_observation"]




