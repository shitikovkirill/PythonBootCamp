import time
import typing
import paramiko
from pbc.selenium.base_grid import BaseGrid


class Grid(BaseGrid):
    def __init__(self, ssh_client): # type: (paramiko.SSHClient) -> None
        self._client = ssh_client

    def download(self, new_file_name, url): # type: (str, str) -> int
        print 'Download'
        stdin, stdout, stderr = self._client.exec_command("wget -O {} {}".format(new_file_name, url), timeout=300)

        while not stdout.channel.exit_status_ready():
            print('.')
            time.sleep(1)
        return stdout.channel.recv_exit_status()

    def is_download(self, file_name): # type: (str) -> bool
        stdin, stdout, stderr = self._client.exec_command('ls {}'.format(file_name))
        selenium_server_file = [line for line in stdout.read().split('\n') if line]
        if len(selenium_server_file) >= 1:
            return True
        else:
            return False

    def start_hub(self): # type: () -> None
        print 'Start hub'
        self._client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')

    def add_node(self): # type: () -> None
        print 'Add node'
        self._client.exec_command(
            'java -jar selenium-server-standalone-3.8.0.jar -role node  -nodeConfig sg-node.json >> log.txt 2>&1 &')


class StartGrid(BaseGrid):
    def __init__(self, grid):
        self._g = grid

    def start_hub(self): # type: () -> None
        self._g.start_hub()

    def download(self, new_file_name, url): # type: (str, str) -> None
        if not self._g.is_download(new_file_name):
            self._g.download(new_file_name, url)

    def add_node(self): # type: () -> None
        self._g.add_node()