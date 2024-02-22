import logging
# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename="demo2.log",datefmt="%d/%m/%s %I:%M:%S %p %A",level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A' , level=logging.DEBUG ,filename="test2.log",filemode="a")
logging.critical("this is critical varsha")
logging.error("this is error")
logging.warning("this is warn")
logging.info("this is info")
logging.debug("this is debug")
