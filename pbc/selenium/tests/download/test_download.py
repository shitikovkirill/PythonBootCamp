import pytest

from pbc.selenium.grids import Grid
from pbc.selenium.tests.assert_checker import assert_count_file


@pytest.mark.download
def test_grid_download(ssh_client):
    assert_count_file(ssh_client, 0)

    grid = Grid(ssh_client)
    grid.download('selenium-server-standalone-3.8.0.jar', 'https://goo.gl/SVuU9X')

    assert_count_file(ssh_client, 1)


@pytest.mark.download
def test_grid_is_download(ssh_client):
    assert_count_file(ssh_client, 0)

    ssh_client.exec_command('touch selenium-server-standalone-3.8.0.jar')

    assert_count_file(ssh_client, 1)

    grid = Grid(ssh_client)
    assert grid.is_download('selenium-server-standalone-3.8.0.jar')
