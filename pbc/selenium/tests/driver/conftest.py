import paramiko
import pytest


@pytest.fixture(scope='session', autouse=True)
def ssh_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect('192.168.33.10', username='vagrant', password='vagrant')
    print 'Open paramiko client'

    yield client

    ssh_client.exec_command('killall -9 java')
    ssh_client.exec_command('rm selenium-server-standalone-3.8.0.jar')
    print 'Close paramiko client'
    client.close()



