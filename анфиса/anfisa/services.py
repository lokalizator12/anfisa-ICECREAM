import requests


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуйте позже>'

def what_temperature(weather):    
    if (weather == '<сетевая ошибка>' or
        weather == '<ошибка на сервере погоды. попробуйте позже>'):
        return weather
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == '-':
            parsed_temperature += char
        try:
            num = int(char)
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature

def what_conclusion(parsed_temperature):
    try:
        # Приведите parsed_temperature к типу int
        # и сохраните полученное число в переменную temperature
        temperature = int(parsed_temperature)
        for char in parsed_temperature:
            if char == '-':
                return f'Берегись простуды, слишком холодно, не сезон для мороженого! '
        if 27< temperature:
            return f'Жарко, как в Африке, нужны две порции!'
        
        elif 18< temperature and temperature <27:
            return f'Порция мороженого сейчас будет в самый раз!'
        
        elif temperature <18 :
            return f'Берегись простуды, слишком холодно, не сезон для мороженого! '
        else:
            return f'Берегись простуды, слишком холодно, не сезон для мороженого! '
        
        
            
    except ValueError:
         return f'Не могу узнать погоду'
