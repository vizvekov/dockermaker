__author__ = 'subadmin'

import docker


class Container():

    def __init__(self, name):
        self.__environment = {}
        self.name = name

    def update_env(self, key, value):
        if key == 'ports':
            self.ports = value
        else:
            self.__environment.update({key: value})

    def start(self):
        print "My name is: %s" % self.name
        print "My external ports: %s" % self.ports
        print "My variables: %s" % self.__environment

    def get_env(self):
        return self.__environment

    def __del__(self):
        pass
