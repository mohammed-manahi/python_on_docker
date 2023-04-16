from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):
    """
    Create simple consumer
    """

    def connect(self):
        self.accept()
        self.send(text_data='You are connected by web sockets!')

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        pass
