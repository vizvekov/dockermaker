__author__ = 'Vadim'

import ConfigParser, re


class Conf():


    def __init__(self,conf_path):
        self.Config = ConfigParser.ConfigParser()
        self.Config.read(conf_path)

    def __del__(self):
        del self.Config

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
