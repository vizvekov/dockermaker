__author__ = 'subadmin'

from classes.container import Container as base_lxc


class Galera(base_lxc):

    ports = [3306, 4567, 4568, 4444]

