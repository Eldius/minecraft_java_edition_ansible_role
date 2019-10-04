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
    assert f.contains(
        "java -Xmx2g -Xms1g -jar " +
        "/servers/minecraft_folder/server.jar nogui")


def test_server_config(host):
    f = host.file('/servers/minecraft_folder/server.properties')
    assert f.exists
    assert f.user == 'minecrafter_user'
    assert f.group == 'minecrafter_user'
    assert f.contains("gamemode=survival")
    assert f.contains("max-players=33")
    assert f.contains("server-port=25565")


def test_eula_file(host):
    f = host.file('/servers/minecraft_folder/eula.txt')
    assert f.exists
    assert f.user == 'minecrafter_user'
    assert f.group == 'minecrafter_user'
    assert f.contains("eula=true")
    assert f.content_string == "eula=true"


def test_service_config(host):
    f = host.file('/etc/systemd/system/minecraft_service.service')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains("ExecStart=/servers/minecraft_folder/start_server.sh")
    assert f.contains("User=minecrafter_user")
    assert f.contains("Description=minecraft_service")


def test_java_installation(host):
    assert host.exists("java")
    version_result = host.run("java -version")
    assert ("build 1.8." in version_result.stdout or
            "build 1.8." in version_result.stderr)
    assert ("OpenJDK 64-Bit Server VM" in version_result.stdout or
            "OpenJDK 64-Bit Server VM" in version_result.stderr)
