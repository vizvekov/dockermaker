__author__ = 'subadmin'

from classes.servers_control.fabric import Fabric
from classes.console import Console
import docker


class Server():

    services_type = ['mysql', 'mq', 'glance', 'keystone']

    def __init__(self, host, port, etcd_ip, int_name = None):
        self.name = int_name if int_name else host
        self.host = host
        self.port = port
        self.etcd_ip = etcd_ip
        self.base_url = "http://%s:%s" % (host, port)
        self.services = {}
        self.roles = {}
        self.fab = Fabric()

    def set_role(self, role_config):
        self.roles.update(role_config)

    def create_service(self, name):
        if not self.__service_validate(name) or self.is_service_here(name):
            return False
        try:
            lxc_obj = self.fab.get_service(name)(name=name)
        except Exception, e:
            print e
            return False
        lxc_obj.update_env(key="HOST_IP",value=self.host)
        lxc_obj.update_env(key='etcd', value=self.etcd_ip)
        for key, value in self.roles[name].iteritems():
            lxc_obj.update_env(key=key, value=value)
        self.services.update({name: lxc_obj})
        return True

    def run_services(self):
        print "My name is: %s" % self.name
        print "Begin starting my services:"
        for service, lxc in self.services.iteritems():
            lxc.start()

    def get_service_status(self,name):
        if not self.__service_validate(name) or not self.is_service_here(name):
            return False
        serv_obj = self.fab.get_service(name)
        if not serv_obj:
            return False



    def is_service_here(self,name):
        try:
            return self.services[name]
        except Exception, e:
            return False

    def __service_validate(self,name):
        return True if name in self.services_type else False

    def __del__(self):
        pass