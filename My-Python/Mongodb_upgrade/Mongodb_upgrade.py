
## Upgrade of Mongodb From 3.2 to 3.4 Version

import subprocess
import logging
import pymongo
import json
import logging
import atexit
import paramiko
from configparser import ConfigParser
import sys
from collections import OrderedDict

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
data_common = json.load(data, object_pairs_hook=OrderedDict)

for k, v in data_common.items():
    v2 = [v1['commandToRun'] for k1, v1 in v.items()]

for key, value in data_common.items():
    value2 = [value1['node'] for key1, value1 in value.items()]
    print value2


def execute_remote():

    data_dict = {}
    config = ConfigParser()
    config.read('config.ini')

    for i in config.options('main'):
        data_dict.update({i: config.get('main',i)})

    for i in value2:

        remote = myssh(i,data_dict['user'],data_dict['password'])

        for cmd in v2:
            out,err,rval = remote(cmd)
            print out

execute_remote()