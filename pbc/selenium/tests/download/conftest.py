import paramiko
import pytest


@pytest.fixture(autouse=True)
def delete_jar_file(ssh_client):
    print('Delete selenium-server-standalone-3.8.0.jar file')
    ssh_client.exec_command('rm selenium-server-standalone-3.8.0.jar')
    yield
    ssh_client.exec_command('rm selenium-server-standalone-3.8.0.jar')

