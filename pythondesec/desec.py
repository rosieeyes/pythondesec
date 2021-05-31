import httpx
import logging

logging.basicConfig(
    filename="pythondesec.log",
    encoding='utf-8',
    format="%(asctime)s %(message)s",
    level=logging.DEBUG
)

class Desec:
    def __init__(self):
        self.httpclient = httpx.Client()
        
        logging.info("Desec Client initialised")