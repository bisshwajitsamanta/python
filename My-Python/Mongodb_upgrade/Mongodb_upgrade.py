
## Upgrade of Mongodb From 3.2 to 3.4 Version

import subprocess
from configparser import ConfigParser


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
    #cmd_mongo = 'mongo --ssl --sslAllowInvalidCertificates --port port -u admin -p --authenticationDatabase username'
    cmd_mongo='systemctl status service'

    for key in data:
        if key in cmd_mongo:
            cmd_mongo = cmd_mongo.replace(key, data[key])
    print "cmd:: ", cmd_mongo

    filename = "Mongodb_upgrade.txt"
    f = open(filename, 'w')

    subprocess.call(cmd_mongo,shell=True, stdout=f)


disable_balancer()







