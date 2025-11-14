import logging

logging.basicConfig(
    level= logging.ERROR,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filename= "logs.log",
    filemode= "w",
    encoding="UTF-8"
)

logging.debug("Func has called")
logging.info("Program has started")
logging.warning("Func is too old")
logging.error("User using wrong login")
logging.fatal("Program has crashed")


assert 2 + 2 == 4, "2 + 2 is not equal 5"

def hello(name):
    '''
    >>> hello("name")
    'Hello, name!'

    >>> hello("Keks")
    'Hello, name!'
    '''
    return f"Hello, {name}!"




