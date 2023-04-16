import time
from django.template.loader import render_to_string
from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer
from datetime import datetime
import threading


class EchoConsumer(WebsocketConsumer):
    """
    Create simple consumer
    """

    def connect(self):
        self.accept()
        self.send(text_data='You are connected by web sockets!')

        def send_current_time(self):
            while True:
                self.send(text_data=str(datetime.now().strftime('%H:%M:%S')))
                time.sleep(1)

        threading.Thread(target=send_current_time, args=(self,)).start()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        pass


class BMIConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive_json(self, data):
        """
        Receive event data
        :param text_data:
        :param bytes_data:
        :return:
        """
        height = data['height'] / 100
        weight = data['weight']
        bmi = round(weight / (height ** 2), 1)
        self.send_json(
            content={
                "action": "BMI result",
                "html": render_to_string("components/_bmi_result.html",
                                         {"height": height, "weight": weight, "bmi": bmi})
            }
        )
