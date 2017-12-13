from abc import ABCMeta, abstractmethod


class BaseGrid:
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_hub(self):
        pass

    @abstractmethod
    def download(self, new_file_name, url):
        pass

    @abstractmethod
    def add_node(self):
        pass
