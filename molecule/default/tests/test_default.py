import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_service_user(host):
    u = host.user("minecrafter_user")
    assert u.exists


def test_hosts_file(host):
    f = host.file('/servers/minecraft_folder')

    assert f.exists
    assert f.is_directory
    assert f.user == 'minecrafter_user'
    assert f.group == 'minecrafter_user'
