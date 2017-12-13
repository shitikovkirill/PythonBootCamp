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
