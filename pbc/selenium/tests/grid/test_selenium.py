import pytest
from pbc.selenium.grids import Grid, StartGrid


@pytest.mark.grid
def test_sg(ssh_client, assert_checker):
    assert_checker.count_of_java_process(0)

    grid = Grid(ssh_client)
    grid.download('selenium-server-standalone-3.8.0.jar', 'https://goo.gl/SVuU9X')
    grid.download('sg-node.json', 'https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/')
    grid.start_hub()
    grid.add_node()

    assert_checker.count_of_java_process(2)


@pytest.mark.grid
def test_sg_sm(ssh_client, assert_checker):
    assert_checker.count_of_java_process(0)

    grid = StartGrid(Grid(ssh_client))
    grid.download('selenium-server-standalone-3.8.0.jar', 'https://goo.gl/SVuU9X')
    grid.download('sg-node.json', 'https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/')
    grid.start_hub()
    grid.add_node()

    assert_checker.count_of_java_process(2)
