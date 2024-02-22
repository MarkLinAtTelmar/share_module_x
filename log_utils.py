import logging

class EngineLog():
    def __init__(self, name) -> None:
        self.__logger = None
        self.__logger_name = name

    def get_logger(self):
        if self.__logger is None:
            self.__logger = logging.getLogger(self.__logger_name)
        return self.__logger

    def print_on_console(self, message):
        print(message)