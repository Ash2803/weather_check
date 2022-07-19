import requests


def get_url():
    cities = ('Череповец', 'Лондон', 'Шереметьево')
    lang = {'lang': 'ru'}
    for city in cities:
        url_template = f'https://wttr.in/{city}'
        response = requests.get(url_template, params=lang)
        response.raise_for_status()
        print(response.text)


print(get_url())
