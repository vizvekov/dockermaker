__author__ = 'Vadim'

import paramiko


class Console():


    def __init__(self, host, passwd=None, key_filename=None, user="root"):
        self.host = host
        self.key_filename = key_filename
        self.passwd = passwd
        self.user = user

    def expoler_system(self):
        self.__detect_os()
        self.__detect_sw()

    def __exec_command(self, cmd):
        con = self.__get_conection()
        stdin, stdout, stderr = con.exec_command(cmd)
        errors = stderr.readlines()
        output = stdout.readlines()
        self.__destroy_connection(con)
        return output if not errors else False

    def __split_out(self, str_list):
        while True:
            try:
                str_list.remove("")
            except ValueError:
                break
        return str_list


    def __detect_os(self):
        command_out = self.__exec_command('cat /etc/centos-release')
        if command_out:
            self.os_type, tmp, self.os_version, tmp = command_out[0].split(' ')

    def __detect_sw(self):
        if self.os_type == 'CentOS':
            out = self.__exec_command('/bin/rpm -qi docker-io')
            if out:
                for line in out:
                    line = self.__split_out(line.split(' '))
                    if line[0] == 'Version':
                        self.docker = line[2]
                        break
            else:
                print "We have some errors"
            if not hasattr(self, 'docker'):
                print "no docker installed"


    def __get_conection(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if not self.passwd:
            client.connect(hostname=self.host, username=self.user, key_filename=self.key_filename)
        else:
            client.connect(hostname=self.host, username=self.user, password=self.passwd)
        return client

    def __destroy_connection(self, client):
        client.close()
        del client

    def __del__(self):
        pass




