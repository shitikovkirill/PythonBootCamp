import pytest

from pbc.selenium.grids import Grid


@pytest.mark.download
def test_grid_download(ssh_client, assert_checker):
    assert_checker.count_file(0)

    grid = Grid(ssh_client)
    grid.download('selenium-server-standalone-3.8.0.jar', 'https://goo.gl/SVuU9X')

    assert_checker.count_file(1)


@pytest.mark.download
def test_grid_is_download(ssh_client, assert_checker):
    assert_checker.count_file(0)

    ssh_client.exec_command('touch selenium-server-standalone-3.8.0.jar')

    assert_checker.count_file(1)

    grid = Grid(ssh_client)
    assert grid.is_download('selenium-server-standalone-3.8.0.jar')
