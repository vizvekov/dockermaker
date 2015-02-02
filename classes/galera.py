__author__ = 'subadmin'

from classes.container import Container as base_lxc


class Galera(base_lxc):

    ports = [3306, 4567, 4568, 4444]

    def start(self, host, port, ssl=False, image_name='galera'):
        http = "http"
        if ssl:
            http = "https"
        url = "%s://%s:%s" % (http, host, port)
        self.c_name = "%s_%s" % (image_name, host)
        self.proposal = self.get_copy(image_name=image_name,
                                                     conrainer_name=self.c_name,
                                                     export_ports=self.ports)
        self.docker_cli.start(self.proposal)

    def stop(self):
        self.docker_cli.stop(self.proposal)