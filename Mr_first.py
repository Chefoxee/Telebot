import requests

bot_adress_get_updates = "https://api.telegram.org/bot6623214117:AAEDFClvKNGQgZsKK78GPFLylniUyR8pdcY/getUpdates"
bot_adress_send_message = "https://api.telegram.org/bot6623214117:AAEDFClvKNGQgZsKK78GPFLylniUyR8pdcY/sendMessage"
last_update_id = 0


def send_weather(city):

    weather_url = "http://api.weatherapi.com/v1"
    get_weather_info = requests.get(f"{weather_url}/current.json?key=35e5486e758e470ea36160515233010&q={city}&aqi=no")
    weather_info_to_json = get_weather_info.json()
    temp_celsius = weather_info_to_json['current']['temp_c']
    weather = weather_info_to_json['current']['condition']['text']
    result = f"Температура: {temp_celsius} градуса по цельсию, погода: {weather}"
    return result


while True:

    get_bot_updates = requests.get(bot_adress_get_updates, params={"offset": last_update_id + 1})
    updates_to_json = get_bot_updates.json()

    for update in updates_to_json['result']:

        last_update_id = update['update_id']
        user_name = update['message']['chat']['first_name']
        user_username = update['message']['chat']['username']
        message_text = update['message']['text']
        print(f"Пользователь {user_name}(@{user_username}) написал боту - \" {message_text} \" ")

        if message_text == "/Погода":

            for update in updates_to_json['result']:

                last_update_id = update['update_id']
                chat_id = update['message']['chat']['id']
                get_city = requests.get(bot_adress_send_message, params={'chat_id': chat_id, 'text': 'Укажите город'})



















