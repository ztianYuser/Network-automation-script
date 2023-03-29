import subprocess

# Connect to remote server via SSH
ssh = subprocess.Popen(["ssh", "root@192.168.133.252", "pwd"],   #输入他要返回的相对的指令
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

# Get the output and error messages
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print("ERROR: %s" % error)
else:
    print(result)
