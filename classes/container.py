__author__ = 'subadmin'

import docker


class Container():

    def __init__(self, url):
        self.docker_cli = docker.Client(base_url=url)

    def get_copy(self, image_name, conrainer_name, export_ports):
        if type(export_ports) is not list():
            return False
        return self.docker_cli.create_container(image=image_name, detach=True, name=conrainer_name, ports=export_ports)

    def __del__(self):
        self.docker_cli.close()
