def test_apt_preferences_docker_compose_file(host):
    f = host.file("/etc/apt/preferences.d/docker-compose")
    assert f.exists
    assert f.is_file


def test_apt_preferences_docker_file(host):
    f = host.file("/etc/apt/preferences.d/docker")
    assert f.exists
    assert f.is_file


def test_systemd_overlay_file(host):
    f = host.file("/etc/systemd/system/docker.service.d/overlay.conf")
    assert f.exists
    assert f.is_file


def test_limits_file(host):
    f = host.file("/etc/security/limits.d/docker.conf")
    assert f.exists
    assert f.is_file


def test_docker_running_and_enabled(host):
    f = host.service("docker")
    assert f.is_running
    assert f.is_enabled


def test_docker_socket(host):
    f = host.file("/var/run/docker.sock")
    assert f.exists
    assert f.is_socket

    o = host.socket("unix:///var/run/docker.sock")
    assert o.is_listening


def test_docker_mountpoint(host, AnsibleDefaults):
    f = host.file("/var/lib/docker")
    assert f.exists
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o711

    m = host.mount_point("/var/lib/docker")
    assert m.exists
    assert m.device == "/dev/loop0"
    assert m.filesystem == AnsibleDefaults["docker_storage_filesystem"]
