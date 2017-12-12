from abc import ABCMeta, abstractmethod


class BaseServer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
