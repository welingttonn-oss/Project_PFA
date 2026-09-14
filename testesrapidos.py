import os
import logging

testando = "Olá mundo, estou aprendendo Loggings"

logging.basicConfig(level=logging.DEBUG)

logging.debug(testando)
logging.info(testando)
logging.warning(testando)
logging.error(testando)
logging.critical(testando)