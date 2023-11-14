# Import required modules/packages/library
import pexpect


# Define variables
ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'


# Create the SSH session
session = pexpect.spawn('ssh ' + username + '@' + ip_address,
encoding='utf-8', timeout=20)
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])


# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()

# Session expecting password, enter details
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering password: ', password)
    exit()


# Enter enable mode
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! entering enable mode')
    exit()
# Send enable password details
session.sendline(password_enable)
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! entering enable mode after sending password')
    exit()


# Enter configuration mode
session.sendline('configure terminal')
result = session.expect([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! entering config mode')
    exit()


# Change the hostname to R1
session.sendline('hostname R1')
result = session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result != 0:
    print('--- Failure! setting hostname')


# Exit config mode
#session.sendline('exit')
# Exit enable mode
#session.sendline('exit')


print('-------------------------------------------------------------------------')
print('')
print('--- You have logged in succesfully! connecting to:', ip_address)
print('---                                      Username: ' , username)
print('---                                      Password: ' , password)
print('')
print('-------------------------------------------------------------------------')

#Set the terminal length to 0
session.sendline('terminal length 0')
result= session.expect(['#'])

# running config
session.sendline("show run brief")
result= session.expect(['#'])
config_info = session.before

#file the running config
outfile = open('config_fileGodfrey.txt', 'w')
outfile.write(config_info)

#Output the running config
print('This is the: ',config_info)
