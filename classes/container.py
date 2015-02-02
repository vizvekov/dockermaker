__author__ = 'subadmin'



class Container():

    def __init__(self, docker_cli, etcd_ip):
        self.docker_cli = docker_cli
        self.__environment = {"etcd": etcd_ip}

    def update_env(self, key, value):
        self.__environment.update({key: value})

    def get_env(self):
        return self.__environment

    def get_copy(self, image_name, conrainer_name, export_ports):
        if type(export_ports) is not list():
            return False
        return self.docker_cli.create_container(image=image_name, detach=True, name=conrainer_name, ports=export_ports,
                                                environment=self.__environment)

    def __del__(self):
        pass
