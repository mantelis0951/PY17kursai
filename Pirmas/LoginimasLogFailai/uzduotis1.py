import math
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('aritmetika3.log')
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def numbersum(*args):
    total = sum(args)
    logger.info(f"Musu skaiciai yra:{myArgs}, ju suma yra: {total}")


myArgs = (1, 4, 2, 5, 7, 8)
numbersum(*myArgs)


def sqrt(number):
    try:
        sqrt_number = math.sqrt(number)
        logger.info(f"Musu skaicius yra: {number} bei jo saknis yra: {int(sqrt_number)}")
        return sqrt_number  # Return the calculated square root
    except TypeError:
        logger.exception("Irasytas ne skaicius")


mySqrt = 'sadasda'
result = sqrt(mySqrt)


def lenofwords():
    sentence = "Labas, mano vardas Mantas"
    return len(sentence), sentence


sentence_length, result1 = lenofwords()

logger.info(f"Panaudotas zodis yra: {sentence_length} Simboliu sakinyje: {result1} ")


def resultof(x, y):
    try:
        result2 = x/y
        logger.info(f"Skaiciu x:{x} padaliname is skaiciaus y:{y} ir gauname atsakyma: {result2}")
    except ZeroDivisionError:
        logger.exception("Dalyba is 0")
    else:
        return result2


resultof(5, 0)
