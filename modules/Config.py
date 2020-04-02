#!/usr/bin/python3
import yaml

class Config:
    """ Base class for all configuration parameters. """

    def __init__(self, filename="../config.yaml"):
        """ Instance constructor
        :param filename: configuration file (yaml formated)
        :return: xxxxxxxxxxxx
        """
        self.filename = filename

        # Append each config parameter to an list
        self.readConfigFile()

    def readConfigFile(self, filename="../config.yaml"):
        """ Read file and add config parameters to instance
        :param filename: config file (yaml formated)
        :return: none
        """
        with open(filename, 'r') as yml_file:
            self.config_json = yaml.load(yml_file)

    def getConfigParameter(self, config_section): # todo: remove config_param
        """ Accessor method for displaying configuration parameters as requested.
        :return: parameter (str)
        """
        return(self.config_json[config_section])


# PoC:
#conf = Config()
#print(conf.getConfigParameter('postgresql'))