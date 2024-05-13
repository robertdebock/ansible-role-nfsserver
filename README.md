# [Ansible role nfsserver](#nfsserver)

Setup exports on an nfs server

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-nfsserver/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-nfsserver/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-nfsserver/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-nfsserver)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/nfsserver)](https://galaxy.ansible.com/robertdebock/nfsserver)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-nfsserver.svg)](https://github.com/robertdebock/ansible-role-nfsserver/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-nfsserver/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.nfsserver
      nfsserver_exports:
        - share: /mnt/export
          owner: root
          group: root
          mode: "0755"
          hosts:
            - name: "10.0.0.0/24"
              options:
                - ro
                - no_subtree_check
                - nohide
            - name: "172.16.0.0/24"
              options:
                - rw
                - sync
                - no_wdelay
        - share: /mnt/export2
          owner: root
          group: root
          mode: "0755"
          hosts:
            - name: "10.2.3.0/24"
              options:
                - ro
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-nfsserver/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-nfsserver/blob/master/defaults/main.yml):

```yaml
---
# defaults file for nfsserver

# You can define a list of exports:
# nfsserver_exports:
#   - share: /mnt/export
#     owner: root
#     group: root
#     mode: "0755"
#     hosts:
#       - name: "10.0.0.0/24"
#         options:
#           - ro
#           - no_subtree_check
#           - nohide
nfsserver_exports: []

# You can write the exports in a specific file.
nfsserver_exports_file: /etc/exports
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-nfsserver/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-nfsserver/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|8, 9|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[opensuse](https://hub.docker.com/r/robertdebock/opensuse)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-nfsserver/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-nfsserver/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
