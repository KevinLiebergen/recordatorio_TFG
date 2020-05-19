import time
import telebot
import json

class Telegram:
    def __init__(self):
        with open('api_telegram.json') as json_file:
            data = json.load(json_file)

            self.token = data['token']
            self.ch_id = data['ch_id']
            self.tb = telebot.TeleBot(self.token)

    def enviar_mensajes_a_telegram(self):
        self.tb.send_message(self.ch_id, "Ya es hora de ponerse\
		con el TFG, escorias")



if __name__ == '__main__':
	teleg = Telegram()
	while(1):
		teleg.enviar_mensajes_a_telegram()
		time.sleep(600) #10 minutos
