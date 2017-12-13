from abc import ABCMeta, abstractmethod


class BaseDriver:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_page(self, url):
        pass
