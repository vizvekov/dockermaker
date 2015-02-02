__author__ = 'Вадим'

from classes.galera import Galera


class Fabric():


    def __init__(self):
        pass

    def get_service(self, name):
        return Galera if name is "mysql" else False

    def __del__(self):
        pass
