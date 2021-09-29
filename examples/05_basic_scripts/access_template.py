#!/usr/bin/env python3

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']


vlan = 5
access_str = "\n".join(access_template)
print(access_str.format(vlan))
