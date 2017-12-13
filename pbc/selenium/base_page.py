from abc import ABCMeta, abstractmethod


class BasePage:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_title(self):
        pass
