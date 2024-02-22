import logging

class EngineLog():
    def __init__(self, name) -> None:
        self.__logger:logging.Logger = None
        self.__logger_name = name

    def get_logger(self) -> logging.Logger:
        if self.__logger is None:
            self.__logger = logging.getLogger(self.__logger_name)
        return self.__logger

    def print_debug_log(self, message):
        self.get_logger().debug(message)