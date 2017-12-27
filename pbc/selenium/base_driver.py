from abc import ABCMeta, abstractmethod


class BaseDriver:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.pages = []

    @abstractmethod
    def get_page(self, url):
        pass

    @abstractmethod
    def close_pages(self):
        pass
