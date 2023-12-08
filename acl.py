session.sendline('configure terminal')
result = session.expect([r'#', pexpect.TIMEOUT])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering configuration mode')
    exit()

session.sendline('access-list 1 permit 192.168.1.0 0.0.0.255 any')
session.expect([r'#', pexpect.TIMEOUT])

session.sendline('interface GigabitEthernet0/0')
session.expect([r'#', pexpect.TIMEOUT])
session.sendline('ip access-group 1 in')
session.expect([r'#', pexpect.TIMEOUT])


session.sendline('end')
session.expect([r'#', pexpect.TIMEOUT])
session.sendline('write memory')
session.expect([r'#', pexpect.TIMEOUT])
