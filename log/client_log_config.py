import logging

logger = logging.getLogger('client')

log_format = logging.Formatter('%(asctime)s- %(levelname)s- %(module)s- %(funcName)s- %(message)s')

client_log = logging.FileHandler(filename="client.log", encoding='utf-8')
client_log.setFormatter(log_format)
client_logger = logging.getLogger("client.log")
client_logger.setLevel(logging.DEBUG)
client_logger.addHandler(client_log)
# client_logger.info('Тестовый запуск логирования')