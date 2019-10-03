Role Name
=========

It's just a role to setup a Minecraft Java Edition server.

Requirements
------------

TODO

Role Variables
--------------

TODO

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
        - {
          role: minecraft-java-edition-ansible-role,
          minecraft_service_user: minecrafter,
          minecraft_install_folder: /servers/minecraft,
          minecraft_max_memory: 1g,
          minecraft_min_memory: 1g,
          minecraft_service_name: minecraft
        }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).