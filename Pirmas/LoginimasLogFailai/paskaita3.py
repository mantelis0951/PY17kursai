import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("aritmetika.log")
logger.addHandler(file_handler)
logger.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def dalyba(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        logger.exception("Dalyba is 0")
    else:
        return result

a = 10
b = 0
padalinom = dalyba(a,b)
logger.info(f"Dalyba: 10/5 = {padalinom}")