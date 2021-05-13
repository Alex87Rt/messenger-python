import os
import logging.handlers

from client.main import helpers

log_format = logging.Formatter('%(asctime)-s %(levelname)-s '
                               '%(module)-s %(funcName)-s %(message)s')

client_logger_name = helpers.CLIENT_LOGGER_NAME
client_log_file = os.path.join(helpers.get_this_script_full_dir(),
                               f'{client_logger_name}.log')
client_log_handler = logging.FileHandler(filename=client_log_file, delay=True)
client_log_handler.setFormatter(log_format)
client_logger = logging.getLogger(client_logger_name)
client_logger.setLevel(logging.DEBUG)
client_logger.addHandler(client_log_handler)
