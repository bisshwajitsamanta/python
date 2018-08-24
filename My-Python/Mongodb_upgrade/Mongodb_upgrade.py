
## Upgrade of Mongodb From 3.2 to 3.4 Version

import subprocess
import logging
import pymongo
import json
import logging
import atexit
import paramiko
from configparser import ConfigParser


class myssh:

    def __init__(self, host, user, password, port=22):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port=port, username=user, password=password)
        atexit.register(client.close)
        self.client = client

    def __call__(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        sshdata = stdout.readlines()
        ssherr = stderr.readlines()
        retval = stdout.channel.recv_exit_status()
        return sshdata, ssherr, retval

data = open('data.json')
data_common = json.load(data)

for k, v in data_common.items():
    for k1, v1 in v.items():
        v2= v1['commandToRun']

print v2

def execute_remote():

    remote=myssh('192.168.124.111','sysops','alcatraz1400')
    cmd = v2
    out,err,ret=remote(cmd)
    print out,err,ret

execute_remote()




