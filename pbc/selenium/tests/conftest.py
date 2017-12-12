import paramiko
import pytest


@pytest.fixture(scope='session', autouse=True)
def ssh_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect('192.168.33.10', username='vagrant', password='vagrant')
    print 'Open paramiko client'

    yield client

    print 'Close paramiko client'
    client.close()


@pytest.fixture
def delete_jar_file(ssh_client):
    print('Delete selenium-server-standalone-3.8.0.jar file')
    ssh_client.exec_command('rm selenium-server-standalone-3.8.0.jar')
    yield
    ssh_client.exec_command('rm selenium-server-standalone-3.8.0.jar')


@pytest.fixture
def kill_all_java_process(ssh_client):
    print('Kill all java process')
    ssh_client.exec_command('killall -9 java')
    yield
    ssh_client.exec_command('killall -9 java')
