
## Upgrade of Mongodb From 3.2 to 3.4 Version

import subprocess
from configparser import ConfigParser
import paramiko


def readParser():

    data_dict = {}
    config=ConfigParser()
    config.read("config.ini")
    port = config.get('main','port')
    username = config.get('main', 'username')
    password = config.get('main','password')
    for i in config.options('main'):
        data_dict.update({i: config.get("main", i)})
    return data_dict

def disable_balancer():

    data = readParser()
    cmd = 'mongo --ssl --sslAllowInvalidCertificates --port port -u admin -p --authenticationDatabase username'
    for key in data:
        if key in cmd:
            cmd = cmd.replace(key, data[key])
    print "cmd:: ", cmd


disable_balancer()





