import requests


def get_url():
    url_template = f'https://wttr.in/{"Череповец"}'
    response = requests.get(url_template)
    response.raise_for_status()
    return response.text


print(get_url())
