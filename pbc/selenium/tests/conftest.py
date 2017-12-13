import paramiko
import pytest

from pbc.selenium.tests.assert_checker import AssertChecker


@pytest.fixture(scope='session', autouse=True)
def ssh_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect('192.168.33.10', username='vagrant', password='vagrant')
    print 'Open paramiko client'

    yield client

    client.exec_command('killall -9 java')
    client.exec_command('rm selenium-server-standalone-3.8.0.jar')
    print 'Close paramiko client'
    client.close()


@pytest.fixture(scope='session', autouse=True)
def assert_checker(ssh_client):
    return AssertChecker(ssh_client)
