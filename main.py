__author__ = 'Vadim'

from classes.confs.Conf import Conf
from classes.servers_control.server import Server

CONFIG = 'C:\Users\subadmin\PycharmProjects\dockermaker\classes\confs\docker.conf'

cnf = Conf(CONFIG)

service_configs = cnf.get_services()

servers = {}

for server in cnf.getservers():
    servers.update({server: Server(host=cnf.ConfigSectionMap(server)["ip"],
                                                  port=cnf.ConfigSectionMap(server)["port"],
                                                  etcd_ip=cnf.ConfigSectionMap("globals")["etcd"],
                                                  int_name=server)})
    roles = cnf.ConfigSectionMap(server)["roles"].split(',')
    for role in roles:
        servers[server].set_role({role: service_configs[role]})
        servers[server].create_service(role)

    servers[server].run_services()






