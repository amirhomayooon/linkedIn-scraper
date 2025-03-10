import requests
from db import get_app_settings


def send_message_to_telegram(chat_id, message_text, button_text, button_url):
    payload = {
        'chat_id': chat_id,
        'text': message_text,
        'reply_markup': {
            'inline_keyboard': [[{
                'text': button_text,
                'url': button_url
            }]]
        }
    }
    token = get_app_settings().telegram_token
    resp = requests.post(
        f'https://api.telegram.org/bot{token}/sendMessage',
        json=payload
    )
    if resp.status_code != 200:
        print(resp.text)

    return resp
