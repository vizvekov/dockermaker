__author__ = 'Vadim'

from classes.confs.Conf import Conf
from classes.servers_control.server import Server

CONFIG = 'd:\\docker.conf'

cnf = Conf(CONFIG)

servers = {}

for server in cnf.getservers():
    servers.update({"name": server,"copy": Server(host=cnf.ConfigSectionMap(server)["ip"],
                                                  port=cnf.ConfigSectionMap(server)["port"],
                                                  etcd_ip=cnf.ConfigSectionMap("DEFAULT")["etcd"])})






