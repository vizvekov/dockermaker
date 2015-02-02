__author__ = 'Vadim'

import ConfigParser, re


class Conf():


    def __init__(self,conf_path):
        self.Config = ConfigParser.ConfigParser()
        print self.Config.read(conf_path)

    def __del__(self):
        del self.Config

    def __get_service_config(self,service_id):
        service = self.ConfigSectionMap("service_%s" % service_id)
        ret_val = {}
        env = {}
        for key, value in service.iteritems():
            if key == "ports":
                ret_val.update({"ports": value.split(',')})
            else:
                env.update({key: value})
        ret_val.update(env)
        return ret_val

    def get_services(self):
        service_dict = {}
        for service_id in self.ConfigSectionMap("globals")["services"].split(','):
            service_dict.update({service_id: self.__get_service_config(service_id)})
        return service_dict


    def getservers(self):
        reObj = re.compile('server_')
        servers = []
        for item in self.Config.sections():
            if(reObj.match(item)):
               servers.append(item)
        return servers


    def ConfigSectionMap(self, section):
        dict1 = {}
        options = self.Config.options(section)
        for option in options:
            try:
                dict1[option] = self.Config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1
