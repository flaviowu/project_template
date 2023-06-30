import logging

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('./app.log', mode='a', encoding='utf-8')
stream_handler = logging.StreamHandler()

formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logging.debug('Mensagem de depuração')
logging.info('Mensagem informativa')
logging.warning('Mensagem de aviso')
logging.error('Mensagem de erro')
logging.critical('Mensagem crítica')
