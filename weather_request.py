import requests


def get_current_weather():
    cities = ('Череповец', 'Лондон', 'Шереметьево')
    request_parameters = {'lang': 'ru'}
    for city in cities:
        url_template = f'https://wttr.in/{city}'
        response = requests.get(url_template, params=request_parameters)
        response.raise_for_status()
        print(response.text)


def main():
    print(get_current_weather())


if __name__ == '__main__':
    main()
