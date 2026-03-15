import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()

def divide(a, b):
    logging.info(f"Dividing {a} by {b}")
    try:
        result = a / b
        logging.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero!")
        return None


divide(10, 2)
divide(5, 0)