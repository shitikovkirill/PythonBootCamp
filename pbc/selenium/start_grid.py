from pbc.selenium.base_grid import BaseGrid


class StartGrid(BaseGrid):
    def __init__(self, grid):
        self._g = grid

    def start_hub(self):
        self._g.start_hub()

    def download(self, new_file_name, url):
        if not self._g.is_download(new_file_name):
            self._g.download(new_file_name, url)

    def add_node(self):
        self._g.add_node()
