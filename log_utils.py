import logging

'''
Engine Log class
'''
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

    def print_on_console(self, message):
        print(message)

    def print_error_log(self, message):
        self.get_logger().error(message)

    def print_hello_world(self):
        self.get_logger().info("hello world")
