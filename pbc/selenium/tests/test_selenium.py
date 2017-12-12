import pytest
import time

from pbc.selenium.grid import Grid
from pbc.selenium.start_grid import StartGrid


def get_lines(lines):
    return [line for line in lines.split('\n') if line]


def assert_count_file(ssh_client, count):
    stdin, stdout, stderr = ssh_client.exec_command('ls selenium-server-standalone-3.8.0.jar')
    selenium_server_file = get_lines(stdout.read())
    assert len(selenium_server_file) == count


def assert_count_of_java_process(ssh_client, count):
    stdin, stdout, stderr = ssh_client.exec_command('pgrep java')
    pid_count = get_lines(stdout.read())

    assert len(pid_count) == count


def test_grid_download(ssh_client, delete_jar_file):
    assert_count_file(ssh_client, 0)

    grid = Grid(ssh_client)
    grid.download('selenium-server-standalone-3.8.0.jar', 'https://goo.gl/SVuU9X')

    assert_count_file(ssh_client, 1)


def test_grid_is_download(ssh_client, delete_jar_file):
    assert_count_file(ssh_client, 0)

    ssh_client.exec_command('touch selenium-server-standalone-3.8.0.jar')

    assert_count_file(ssh_client, 1)

    grid = Grid(ssh_client)
    assert grid.is_download('selenium-server-standalone-3.8.0.jar')

@pytest.mark.dev
def test_grid_start_hub(ssh_client, kill_all_java_process):
    assert_count_of_java_process(ssh_client, 0)

    grid = Grid(ssh_client)
    grid.download('selenium-server-standalone-3.8.0.jar', 'https://goo.gl/SVuU9X')
    grid.start_hub()
    time.sleep(5)

    assert_count_of_java_process(ssh_client, 1)


def test_sg(ssh_client, delete_jar_file, kill_all_java_process):
    grid = Grid(ssh_client)
    grid.download('selenium-server-standalone-3.8.0.jar', 'https://goo.gl/SVuU9X')
    grid.download('sg-node.json', 'https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/')
    grid.start_hub()
    grid.add_node()

    assert_count_of_java_process(ssh_client, 2)


def test_sg_sm(ssh_client, delete_jar_file, kill_all_java_process):
    grid = StartGrid(Grid(ssh_client))
    grid.download('selenium-server-standalone-3.8.0.jar', 'https://goo.gl/SVuU9X')
    grid.download('sg-node.json', 'https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/')
    grid.start_hub()
    grid.add_node()

    assert_count_of_java_process(ssh_client, 2)
