import logging
# logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]

)
logger=logging.getLogger("ArithmethicAPP")
def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b}",result)
    return result
def subract(a,b):
    result=a-b
    logger.debug(f"Subtracting{a}-{b}={result}")
    return result

def multply

