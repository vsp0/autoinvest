from lib import currencies
from lib import mailing
import json
import time

users = json.load(open('./data/users.json'))

while True:
    for user in users:
        value = float(users[user]['value'])
        your_btc = float(users[user]['your_btc'])
        
        if users[user]['currency'] == 'BTC':
            if your_btc >= value + your_btc:
                email_content = f'Hello!\n\nYour bitcoins are now worth {value + your_btc} BTC.\n\n -AutoInvest'

                mailing.send_email(user['email_sender'], user['email_passwd'], user['email_recipient'], email_content)
        
        elif users[user]['currency'] == 'EUR':
            converted_to_eur = your_btc * currencies.get_latest_btc()

            if converted_to_eur >= value + converted_to_eur:
                email_content = f'Hello!\n\nYour bitcoins are now worth {value + converted_to_eur} EUROS.\n\n -AutoInvest'

                mailing.send_email(user['email_sender'], user['email_passwd'], user['email_recipient'], email_content)


    time.sleep(3)
