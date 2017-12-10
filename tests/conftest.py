import paramiko
import pytest
from pbc_app.fibonacci import fibonacci_generator


@pytest.yield_fixture(scope='session', autouse=True)
def paramiko_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect('192.168.33.10', username='vagrant', password='vagrant')
    print 'Open paramiko client'

    yield client

    print 'Close paramiko client'
    client.close()


@pytest.yield_fixture(scope='session', autouse=True)
def setup(paramiko_client):
    """
    Up remote Selenium server
    :param paramiko_client:
    :return:
    """
    def get_lines(lines):
        return [line for line in lines.split('\n') if line]

    stdin, stdout, stderr = paramiko_client.exec_command("ls selenium-server-standalone-3.8.0.jar")
    selenium_server_file = get_lines(stdout.read())

    if not selenium_server_file:
        print 'Loading selenium server file'
        paramiko_client.exec_command("wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X", timeout=10)

    paramiko_client.exec_command('pkill java')
    stdin, stdout, stderr = paramiko_client.exec_command('pgrep java')
    pid_count = get_lines(stdout.read())

    try:
        if len(pid_count) == 0:
            paramiko_client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &')
        else:
            raise Exception('You mast kill java process before running script. Restart the tests')

        stdin, stdout, stderr = paramiko_client.exec_command('pgrep java')
        pid_count = get_lines(stdout.read())

        if len(pid_count) == 1:
            paramiko_client.exec_command('java -jar selenium-server-standalone-3.8.0.jar -role node  -hub http://localhost:4444/grid/register >> log.txt 2>&1 &')
        elif len(pid_count) == 0:
            raise Exception('Hub not running.')

        stdin, stdout, stderr = paramiko_client.exec_command('pgrep java')
        pid_count = get_lines(stdout.read())

        if len(pid_count) == 2:
            print 'All process running'
        elif len(pid_count) == 1:
            raise Exception('Node not running.')
    finally:
        paramiko_client.exec_command('pkill java')

    yield None

    print 'Close Selenium server'
    paramiko_client.exec_command('pkill java')


@pytest.fixture(scope='module')
def fib_generator():
    return fibonacci_generator()


@pytest.fixture(scope='module')
def negative_fib_generator():
    return fibonacci_generator(negative=True)
