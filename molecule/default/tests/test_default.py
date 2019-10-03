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


def test_installation_folder(host):
    f = host.file('/servers/minecraft_folder')

    assert f.exists
    assert f.is_directory
    assert f.user == 'minecrafter_user'
    assert f.group == 'minecrafter_user'


def test_jar_file(host):
    f = host.file('/servers/minecraft_folder/server.jar')
    assert f.exists
    assert f.user == 'minecrafter_user'
    assert f.group == 'minecrafter_user'


def test_startup_script(host):
    f = host.file('/servers/minecraft_folder/start_server.sh')
    assert f.exists
    assert f.user == 'minecrafter_user'
    assert f.group == 'minecrafter_user'
    f.contains(
        "java -Xmx2g -Xms1g -jar " +
        "/servers/minecraft_folder/server.jar nogui")


def test_service_config(host):
    f = host.file('/etc/systemd/system/minecraft_service.service')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    f.contains("ExecStart=/servers/minecraft_folder/start_server.sh")
    f.contains("User=minecrafter_user")
