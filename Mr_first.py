import requests

import yaml

with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


tg_endpoint = config['telegram']['endpoint']
tg_token = config['telegram']['token']
weather_endpoint = config['weather_api']['endpoint']
weather_key = config['weather_api']['key']



bot_adress_get_updates = f"https://{tg_endpoint}/bot{tg_token}/getUpdates"
bot_adress_send_message = f"https://{tg_endpoint}/bot{tg_token}/sendMessage"
last_update_id = 0


def get_weather(city):

    weather_url = f"http://{weather_endpoint}/v1"
    get_weather_info = requests.get(f"{weather_url}/current.json?key={weather_key}&q={city}&aqi=no")
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



















