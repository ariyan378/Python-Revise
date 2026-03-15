import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#logging.debug("Starting program")
# logging.info("User logged in")
# logging.warning("Low battery")
# logging.error("File not found")
# logging.critical("System crashed")

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
