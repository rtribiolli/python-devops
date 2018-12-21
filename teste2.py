import paramiko 

client = paramiko.client.SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    'ip',
    username='',
    password=''
)

stin, stdout, sterr = client.exec_command("ls -la")

if stdout.channel.recv_exit_status() = 0:
    print(stdout.read().decode('utf-8'))
else:
    print(sterr.read().decode('utf-8'))






























