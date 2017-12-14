import pytest
import time


@pytest.fixture(autouse=True)
def kill_all_java_process(ssh_client):
    print('Kill all java process')
    ssh_client.exec_command('killall -9 java')
    time.sleep(5)
    yield
    ssh_client.exec_command('killall -9 java')