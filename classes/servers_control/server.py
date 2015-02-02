__author__ = 'subadmin'

from classes.servers_control.fabric import Fabric
import docker


class Server():

    services_type = ['mysql', 'mq', 'glance']

    def __init__(self, host, port, etcd_ip, int_name = None):
        self.name = int_name if int_name else "No name"
        self.host = host
        self.port = port
        self.etcd_ip = etcd_ip
        base_url = "http://%s:%s" % (host, port)
        self.connection = docker.Client(base_url=base_url)
        self.services = {}
        self.fab = Fabric()

    def create_service(self, name):
        if not self.__service_validate(name) or self.is_service_here(name):
            return False
        self.services.update({name: True})
        try:
            serv_obj = self.fab.get_service(name)(docker_cli=self.connection, etcd_ip=self.etcd_ip)
        except:
            print "Cannot get obj of service class %s" % name
        serv_obj.update_env("HOST_IP", self.host)
        serv_obj.start(host=self.host, port=self.port)
        ## Some service processing


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