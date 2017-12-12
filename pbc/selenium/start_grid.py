from pbc.selenium.server import BaseServer


class StartGrid(BaseServer):
    def __init__(self, grid):
        self._g = grid

    def start_hub(self):
        self._g.start_hub()

    def download(self):
        if not self._g.is_download():
            self._g.download()

    def add_node(self):
        self._g.add_node()
