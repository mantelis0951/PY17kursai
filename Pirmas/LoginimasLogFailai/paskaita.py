import logging
import paskaita2
#logging.basicConfig(level=logging.DEBUG, filename="aritmetika.log", format="%(asctime)s:%(levelname)s:%(message)s")
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("aritmetika.log")
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
def dalyba(a,b):
    return a/b

a = 10
b = 5

result = dalyba(10,5)
logging.debug(f"Dalyba: 10/5 = {result}")