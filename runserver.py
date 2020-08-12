from lib import currencies
from lib import mailing
import json
import time

users = json.load(open('./data/users.json'))

def btc_to_eur(btc):
    return btc * currencies.get_latest_btc()

def eur_to_btc(eur):
    return eur / currencies.get_latest_btc()

while True:
    for user in users:
        value = users[user]['value']
        your_btc = users[user]['your_btc']
        past_value = users[user]['past_btc_value']
        
        if users[user]['currency'] == 'BTC':
            if btc_to_eur(your_btc) >= value + your_btc * past_value:
                email_content = f'Hello!\n\nYour bitcoins are now worth {value + your_btc} BTC or {value + btc_to_eur(your_btc)}.\n\n -AutoInvest'

                mailing.send_email(users[user]['email_sender'], users[user]['email_passwd'], users[user]['email_recipient'], email_content)
        
        elif users[user]['currency'] == 'EUR':
            now_converted = btc_to_eur(your_btc)
            past_converted = your_btc * past_value

            if now_converted >= value + past_converted:
                email_content = f'Hello!\n\nYour bitcoins are now worth {eur_to_btc(value) + your_btc} BTC or {value + now_converted}.\n\n -AutoInvest'

                mailing.send_email(users[user]['email_sender'], users[user]['email_passwd'], users[user]['email_recipient'], email_content)

    time.sleep(60)
