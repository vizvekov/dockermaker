__author__ = 'subadmin'


class Server():


    def __init__(self, host, port, int_name = None):
        self.name = int_name if int_name else "No name"
        self.host = host
        self.port = port
        self.services = {}

    def create_service(self, name):
        self.services.update({name: True})
        ## Some service processing


    def is_service_here(self,name):
        return self.services.get(name)

    def __del__(self):
        pass