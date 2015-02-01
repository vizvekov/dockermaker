__author__ = 'subadmin'

import classes.container as base_lxc
import docker


class Galera(base_lxc):

    ports = [3306, 4567]

    def start(self, host, port, ssl=False, image_name='galera'):
        http = "http"
        if ssl:
            http = "https"
        url = "%s://%s:%s" % (http, host, port)
        self.c_name = "%s_%s" % (image_name, host)
        self.proposal = super(Galera, self).get_copy(image_name=image_name,
                                                     conrainer_name=self.c_name,
                                                     export_ports=self.ports)
        super(Galera, self).docker_cli.start(self.proposal)

    def stop(self):
        super(Galera, self).docker_cli.stop(self.proposal)