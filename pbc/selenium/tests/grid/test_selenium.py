import pytest
from pbc.selenium.grids import Grid, StartGrid
from pbc.selenium.tests.assert_checker import assert_count_of_java_process


@pytest.mark.grid
def test_sg(ssh_client):
    assert_count_of_java_process(ssh_client, 0)

    grid = Grid(ssh_client)
    grid.download('selenium-server-standalone-3.8.0.jar', 'https://goo.gl/SVuU9X')
    grid.download('sg-node.json', 'https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/')
    grid.start_hub()
    grid.add_node()

    assert_count_of_java_process(ssh_client, 2)


@pytest.mark.grid
def test_sg_sm(ssh_client):
    assert_count_of_java_process(ssh_client, 0)

    grid = StartGrid(Grid(ssh_client))
    grid.download('selenium-server-standalone-3.8.0.jar', 'https://goo.gl/SVuU9X')
    grid.download('sg-node.json', 'https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/')
    grid.start_hub()
    grid.add_node()

    assert_count_of_java_process(ssh_client, 2)
