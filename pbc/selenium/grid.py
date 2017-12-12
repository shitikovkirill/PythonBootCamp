import time
from pbc.selenium.base_grid import BaseGrid


class Grid(BaseGrid):
    def __init__(self, ssh_client):
        self._client = ssh_client

    def download(self, new_file_name, url):
        print 'Download'
        stdin, stdout, stderr = self._client.exec_command("wget -O {} {}".format(new_file_name, url), timeout=300)

        while not stdout.channel.exit_status_ready():
            print('.')
            time.sleep(1)
        return stdout.channel.recv_exit_status()

    def is_download(self, file_name):
        stdin, stdout, stderr = self._client.exec_command('ls selenium-server-standalone-3.8.0.jar')
        selenium_server_file = [line for line in stdout.read().split('\n') if line]
        if len(selenium_server_file) >= 1:
            return True
        else:
            return False

    def start_hub(self):
        print 'Start hub'
        self._client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')

    def add_node(self):
        print 'Add node'
        self._client.exec_command(
            'java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')
