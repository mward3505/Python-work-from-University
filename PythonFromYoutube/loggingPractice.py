import logging
import math

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="G:\\Documents\\python\\lumberjack.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()


# Test messages
# logger.debug("this is a harmless debug message.")
# logger.info("Just some useful info.")
# logger.warning("I'm sorry, but I can't do that, Dave.")
# logger.error("Did you just try to divide by zero?")
# logger.critical("The entire internet is down!!")
# print(logger.level)


def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0"""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminate
    logger.debug("# compute the discriminant")
    disc = b ** 2 - 4 * a * c

    # Compute the two roots
