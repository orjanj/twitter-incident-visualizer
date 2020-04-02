#!/usr/bin/python3
import yaml

class Config:
    """ Base class for all configuration parameters. """

    def __init__(self, filename="config/config.yaml"):
        """ Instance constructor
        :param filename: configuration file (yaml formated)
        """
        self.filename = filename

        # Append each config parameter to an list
        self.readConfigFile()

    def readConfigFile(self):
        """ Read file and add config parameters to instance
        :param filename: config file (yaml formated)
        """
        with open(self.filename, 'r') as yml_file:
            self.config_json = yaml.load(yml_file)

    def getConfigParameter(self, config_section): # todo: remove config_param
        """ Accessor method for displaying configuration parameters as requested.
        :return: parameter (str)
        """
        return(self.config_json[config_section])