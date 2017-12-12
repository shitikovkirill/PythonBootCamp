import pytest
import time

from pbc.selenium.grid import Grid
from pbc.selenium.start_grid import StartGrid


def get_lines(lines):
    return [line for line in lines.split('\n') if line]


def test_grid_download(ssh_client, delete_jar_file):
    stdin, stdout, stderr = ssh_client.exec_command('ls selenium-server-standalone-3.8.0.jar')
    selenium_server_file = get_lines(stdout.read())
    assert len(selenium_server_file) == 0

    grid = Grid(ssh_client)
    grid.download()

    stdin, stdout, stderr = ssh_client.exec_command('ls selenium-server-standalone-3.8.0.jar')
    selenium_server_file = get_lines(stdout.read())
    assert len(selenium_server_file) == 1


def test_grid_is_download(ssh_client, delete_jar_file):
    stdin, stdout, stderr = ssh_client.exec_command('ls selenium-server-standalone-3.8.0.jar')
    selenium_server_file = get_lines(stdout.read())
    assert len(selenium_server_file) == 0

    ssh_client.exec_command('touch selenium-server-standalone-3.8.0.jar')

    stdin, stdout, stderr = ssh_client.exec_command('ls selenium-server-standalone-3.8.0.jar')
    selenium_server_file = get_lines(stdout.read())
    assert len(selenium_server_file) == 1

    grid = Grid(ssh_client)
    assert grid.is_download()


def test_grid_start_hub(ssh_client, kill_all_java_process):
    stdin, stdout, stderr = ssh_client.exec_command('pgrep java')
    pid_count = get_lines(stdout.read())

    assert len(pid_count) == 0

    grid = Grid(ssh_client)
    grid.start_hub()
    time.sleep(5)

    stdin, stdout, stderr = ssh_client.exec_command('pgrep java')
    pid_count = get_lines(stdout.read())

    assert len(pid_count) == 1


def test_sg(ssh_client, delete_jar_file, kill_all_java_process):
    grid = Grid(ssh_client)
    grid.download()
    grid.start_hub()
    grid.add_node()

    stdin, stdout, stderr = ssh_client.exec_command('pgrep java')
    pid_count = get_lines(stdout.read())
    assert len(pid_count) == 2


@pytest.mark.dev
def test_sg_sm(ssh_client, delete_jar_file, kill_all_java_process):
    grid = StartGrid(Grid(ssh_client))
    grid.download()
    grid.start_hub()
    grid.add_node()

    stdin, stdout, stderr = ssh_client.exec_command('pgrep java')
    pid_count = get_lines(stdout.read())
    assert len(pid_count) == 2
