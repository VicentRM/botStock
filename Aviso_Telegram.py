import requests

def telegram_bot_sendtext(bot_message):

    bot_token = '2089233941:AAFA_md4pvCXgVCB68wkhiOBLc4POIlcDPA'
    bot_chatID = '5246369'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


test = telegram_bot_sendtext("Holaaa! Hay stock, corre!")
#print(test)