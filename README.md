# ansible-faker - v0.4.0-alpha

[![Ansible Role](https://img.shields.io/ansible/role/45692)](https://galaxy.ansible.com/fititnt/faker)

**[working-draft] Faker is a Ansible role that generates fake data for you.
Inspired on [PHP Faker](https://github.com/fzaninotto/Faker). Initial work from
[ansible-syntactic-sugar](https://github.com/fititnt/ansible-syntactic-sugar)**

> **Warning: this is a pre-release**. Variable naming conventions may change.
Feedback is welcome!

<!--
**[not-production-ready] AP-ALB Extras is a well tested cross-platform Ansible
role that implements non-core and testing features for
[AP-ALB Role](https://github.com/fititnt/ap-application-load-balancer), but as
independent role it can be used by other proposes.**

Note: this project may eventually be renamed.
-->

---

<!-- TOC depthFrom:2 -->

- [Requirements](#requirements)
- [Role Variables](#role-variables)
    - [Public APIs](#public-apis)
        - [`faker_sample_content_cdns`](#faker_sample_content_cdns)
        - [`faker_sample_content_static_sites`](#faker_sample_content_static_sites)
        - [`faker_sample_content_phps`](#faker_sample_content_phps)
        - [`faker_devel_nginx_*`](#faker_devel_nginx_)
    - [Special APIs](#special-apis)
        - [`faker_autoinstall_dependencies`](#faker_autoinstall_dependencies)
        - [`faker_autoinstall_repositories`](#faker_autoinstall_repositories)
        - [faker_default_*](#faker_default_)
            - [`faker_default_user`](#faker_default_user)
            - [`faker_default_group`](#faker_default_group)
            - [`faker_default_directory_mode`](#faker_default_directory_mode)
            - [`faker_default_file_mode`](#faker_default_file_mode)
    - [Internal variables](#internal-variables)
- [Dependencies](#dependencies)
- [Example Playbooks](#example-playbooks)
    - [Minimal Playbook](#minimal-playbook)
    - [Playbook using all Public APIs](#playbook-using-all-public-apis)
    - [Playbook full example with Continuos Integration and testinfra](#playbook-full-example-with-continuos-integration-and-testinfra)
- [License](#license)
    - [ansible-faker](#ansible-faker)
    - [files/static-site](#filesstatic-site)

<!-- /TOC -->

---

<!--
The main objective of this role is add some functionality (for example, very
simple configuration of PHP, Python, Java, Tomcat, ...) using a sintax that
reuse variables of the core role, ap-application-load-balancer, and at least
for some very basic cases or very fast bootstraping do not need use others well
know dedicated Ansible Roles.

If you really heavily on some of these extra features consider search for
<https://github.com/topics/ansible-role>.
-->

## Requirements

<!--
Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.
-->

**None.**

This role does not require anything over the averange for an Ansible role.

## Role Variables

<!--
A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.
-->

### Public APIs

#### `faker_sample_content_cdns`
> Deploy sample content on target paths designed to test a CDN (Content
Delivery Network).

**List of paths to deploy sample content of [files/videos](files/videos) and [files/images](files/images)**.
Values from Ansible module [copy](https://docs.ansible.com/ansible/latest/modules/copy_module.html).

#### `faker_sample_content_static_sites`
> Deploy sample content of HTML+CSS+JS static website on target paths to be be
used as test. The string `Hello, world!` is granteed to always exist.

**List of paths to deploy sample content of [files/static-site](files/static-site)**.
Values from Ansible module [copy](https://docs.ansible.com/ansible/latest/modules/copy_module.html).

#### `faker_sample_content_phps`
> Deploy sample content of PHP files on target paths to be used to test if PHP
is working.

**List of paths to deploy sample content of [files/php](files/php)**.
Values from Ansible module [copy](https://docs.ansible.com/ansible/latest/modules/copy_module.html).

#### `faker_devel_nginx_*`

### Special APIs

#### `faker_autoinstall_dependencies`
- Default: `false`

Some A2S public APIs may require packages that already are not automaticaly
installed with Ansible. With this option set to true/yes A2S will install for
you.

#### `faker_autoinstall_repositories`
- Default: `false`

Some A2S public APIs may require dependencies that are not available on some
versions of operational systems without installation of some external
repositories. With this option set to true/yes A2S will autoinstall for
you.

<!--
--- ### Defaults

See [defaults/main.yml](defaults/main.yml).

The variables on this file, different from the ones of _Internal variables_
that have a more strong suggestion based on Operational System, may extend
features of the _Public APIs_.

-->

#### faker_default_*
The default values from `faker_default_*` exist to provide consistence
across operational systems and will be used in some places if you did not
explicitly provide a value.

<!--
> **backward compatibility notice**: the values from `faker_default_*`
> **may** be updated betwen minor versions ("MINOR" on the `MAJOR.MINOR.PATCH`
> format of [SemVer](https://semver.org/) intead of just majors versions of the
> AP-ALB-Extras. If you have strong requeriments, we recommend you to either
> enforce values on your playbooks OR (if want every place to explicitly not
> depend on these defaults) set then to invalid values so any missing try will
> raise imediate errors.

> **Security notice**: these defaults (similar to the default permissions
> permissions of commands like `mkdir`) may be insecure in some contexts. Even
> if you customize them, user/owner and groups are likely depend of the more
> specific case.
-->

##### `faker_default_user`
##### `faker_default_group`
##### `faker_default_directory_mode`
##### `faker_default_file_mode`

### Internal variables

For internal variables based on OS, check [vars/README.md](vars/README.md).

## Dependencies

<!--
A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.
-->

**None.**

This role does not depend on other Ansible roles. Not even the
[ap-application-load-balancer](https://github.com/fititnt/ap-application-load-balancer).

## Example Playbooks

### Minimal Playbook

> Note: If you run this role without explicitly
> use any [Public APIs](#public-apis) (variables starte with `faker_` that
> are not defaults) this Ansible role will make no changes on your system.

```yaml
# Note: this playbook will run without errors, but will not make changes. You
#       need to specify variables
- hosts: all
  roles:
    - { role: fititnt.ansible-syntactic-sugar }
```

### Playbook using all Public APIs

```yaml
- hosts: all
  remote_user: root
  vars:

    faker_sample_content_static_sites:
      - path: /home/user2/public_html
        user: user2

    # faker_iswindows: true # Uncomment next variable only for Windows hosts.
  roles:
    - { role: fititnt.faker }
```
### Playbook full example with Continuos Integration and testinfra

Check the contents of [molecule/default/playbook.yml](molecule/default/playbook.yml)
and our Travis-CI panel at <https://travis-ci.com/fititnt/ap-application-load-balancer-extras>.

If you are not developing an interface that other people depend on or have a
very serius infrastructure or several people making changes, well written
Ansible playbooks may already be great. If this is not sufficient, check our
testinfra tests file at
[molecule/default/tests/test_default.py](molecule/default/tests/test_default.py).

## License
This Ansible role have content from several places with different licenses and
authors.

### ansible-faker

[![Public Domain](https://i.creativecommons.org/p/zero/1.0/88x31.png)](UNLICENSE)

To the extent possible under law, [Emerson Rocha](https://github.com/fititnt)
has waived all copyright and related or neighboring rights to this work to
[Public Domain](UNLICENSE).

### files/static-site
**Code licensed MIT, docs CC BY 3.0.**

[files/static-site/index.html](files/static-site/index.html) and it's assets are
Sample Content from Bootstrap documentation. Source:
<https://v4-alpha.getbootstrap.com/examples/jumbotron/>
