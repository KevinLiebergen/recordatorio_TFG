import telebot
import time
import json
import os



class Telegram:
    def __init__(self, script_dir):
        with open(script_dir + '/api_telegram.json') as json_file:
            data = json.load(json_file)

            self.token = data['token']
            self.ch_id = data['ch_id']
            self.tb = telebot.TeleBot(self.token)

    def enviar_mensajes_a_telegram(self):
        self.tb.send_message(self.ch_id, "Puto Luis termina con tu TFG de una vez")



if __name__ == '__main__':
        script_dir = os.path.dirname(os.path.abspath(__file__))
	
        teleg = Telegram(script_dir)
        teleg.enviar_mensajes_a_telegram()
