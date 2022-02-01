import logging
import math
import coloredlogs

coloredlogs.install(milliseconds=True)

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('mylogger.log')
logger.addHandler(file_handler)
logger.setLevel(level=logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(funcName)s:%(lineno)d:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def ultimate_sum(*args):
  logger.info(f"Sum of numbers {args} eaqual {sum(args)}")

def root(a):
  try:
    logger.info(f"Square root of {a} is {math.sqrt(a)}")
  except TypeError:
    logger.exception(TypeError)

def how_long(string):
  logger.info(f"Length of '{string}' is {len(string)} chars.")

def division(a, b):
  try:
    logger.info(f"{a} / {b} = {a / b}")
  except TypeError:
    logger.exception("a and b should be numbers")
  except ZeroDivisionError:
    logger.exception("b can not be equal to ZERO")

ultimate_sum(5, 4, 3, 2, 1)
root(25)
root("a")
how_long("Si vis pacem, para bellum")
division(15, 3)
division(15, 0)
