import pytest
from pbc.selenium.grids import StartGrid, Grid


@pytest.fixture(scope='module', autouse=True)
def up_grid(ssh_client):
    grid = StartGrid(Grid(ssh_client))
    grid.download('selenium-server-standalone-3.8.0.jar', 'https://goo.gl/SVuU9X')
    grid.download('sg-node.json', 'https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/')
    grid.start_hub()
    grid.add_node()
