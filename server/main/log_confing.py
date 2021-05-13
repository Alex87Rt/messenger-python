import os
import logging.handlers

from server.main import helpers

log_format = logging.Formatter('%(asctime)-s %(levelname)-s '
                               '%(module)-s %(funcName)-s %(message)s')

server_logger_name = helpers.SERVER_LOGGER_NAME
server_log_file = os.path.join(helpers.get_this_script_full_dir(),
                               f'{server_logger_name}.log')
server_log_handler = \
    logging.handlers.TimedRotatingFileHandler(filename=server_log_file,
                                              when='D',
                                              interval=1,
                                              delay=True)
server_log_handler.setFormatter(log_format)
server_logger = logging.getLogger(server_logger_name)
server_logger.setLevel(logging.INFO)
server_logger.addHandler(server_log_handler)
