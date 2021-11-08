import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_exports_content(host):
    expected_exports_content = """#
# Ansible managed: Do NOT edit this file manually!
#

/mnt/export 10.0.0.0/24(ro,no_subtree_check,nohide) 172.16.0.0/24(rw,sync,no_wdelay) """
    exports_content = host.file("/etc/exports").content_string
    assert expected_exports_content == exports_content
