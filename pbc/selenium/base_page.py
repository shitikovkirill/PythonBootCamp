from abc import ABCMeta, abstractmethod


class BasePage:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def source(self):
        pass

    @abstractmethod
    def screenshot(self, name):
        pass

    @abstractmethod
    def enter_data(self, input_el_name, value, button):
        pass

    @abstractmethod
    def close(self):
        pass
