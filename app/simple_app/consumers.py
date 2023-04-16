import time

from channels.generic.websocket import WebsocketConsumer
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
