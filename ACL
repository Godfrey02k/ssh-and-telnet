session.sendline('access-list 1 permit any any')
session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

session.sendline('interface GigabitEthernet0/0')
session.expect([r'R1\(config-if\)#', pexpect.TIMEOUT, pexpect.EOF])
session.sendline('ip access-group 1 in')
session.expect([r'R1\(config-if\)#', pexpect.TIMEOUT, pexpect.EOF])


session.sendline('end')
session.expect([r'#', pexpect.TIMEOUT, pexpect.EOF])
session.sendline('write memory')
session.expect([r'#', pexpect.TIMEOUT, pexpect.EOF])
