def get_lines(lines):
    return [line for line in lines.split('\n') if line]


class AssertChecker:
    def __init__(self, ssh_client):
        self._ssh_client = ssh_client

    def count_file(self, count):
        stdin, stdout, stderr = self._ssh_client.exec_command('ls selenium-server-standalone-3.8.0.jar')
        selenium_server_file = get_lines(stdout.read())
        assert len(selenium_server_file) == count

    def count_of_java_process(self, count):
        stdin, stdout, stderr = self._ssh_client.exec_command('pgrep java')
        pid_count = get_lines(stdout.read())

        assert len(pid_count) == count
