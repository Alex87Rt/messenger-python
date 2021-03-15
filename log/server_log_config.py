import logging

logger = logging.getLogger('server')
format = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s- %(message)s')


server_log = logging.FileHandler(filename="server.log", encoding='utf-8')
server_log.setFormatter(format)
server_logger = logging.getLogger("server.log")
server_logger.setLevel(logging.DEBUG)
server_logger.addHandler(server_log)
#