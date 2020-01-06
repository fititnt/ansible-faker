import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root' or f.group == 'wheel'


def test_hosts_resolve_adress(host):
    site_a_local = host.addr("site-a.local")
    assert site_a_local.is_resolvable
    assert '127.0.0.1' in site_a_local.ipv4_addresses

    cdn_site_a_local = host.addr("cdn.site-a.local")
    assert cdn_site_a_local.is_resolvable
    assert '127.0.0.1' in cdn_site_a_local.ipv4_addresses


def test_groups(host):
    assert host.group("cdns").exists
    # assert host.group("group1").exists


def test_users_user(host):
    assert host.user("fititnt").exists
    assert host.user("cdn-site-b").exists
    assert host.user("fititnt").exists
    assert "cdns" in host.user("cdn-site-a").groups
    assert "cdns" in host.user("cdn-site-b").groups


def test_users_authorized_key(host):
    f = host.file('/home/fititnt/.ssh/authorized_keys')

    assert f.exists
    assert f.user == 'fititnt'
    assert f.group == 'fititnt'


def test_sample_content_cdns(host):
    fa = host.file('/home/cdn-site-a/public_html/index.html')
    assert fa.exists
    assert fa.user == 'cdn-site-a'
    assert fa.group == "cdns"

    fb = host.file('/home/cdn-site-b/public_html/index.html')
    assert fb.exists
    assert fb.user == 'cdn-site-b'
    assert fb.group == "cdns"


def test_devel_nginx_is_installed(host):
    assert host.package("nginx").is_installed


def test_devel_nginx_is_enabled(host):
    is_conteiner = 'ISCONTEINER' in os.environ
    assert not is_conteiner or host.service("nginx").is_enabled


def test_devel_nginx_is_running(host):
    assert host.service("nginx").is_running
