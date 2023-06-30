import logging
import logging.config
import configparser

# Ler as configurações do arquivo INI
config = configparser.ConfigParser()
config.read('logging_config.ini')

# Configurar o logger usando as configurações do arquivo INI
logging.config.fileConfig('logging_config.ini')

# Usar o logger
logger = logging.getLogger('')
logger.debug('Mensagem de depuração')
logger.info('Mensagem informativa')
logger.warning('Mensagem de aviso')
