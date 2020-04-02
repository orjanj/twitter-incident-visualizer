#!/usr/bin/python3
import googlemaps
from Config import Config # TODO: Make it prettier

class Gmaps:
    """ Base class for connecting and fetching data from Google Maps API. """

    def __init__(self):
        """ Instance constructor
        :return: none
        """
        config = Config()
        config_param = config.getConfigParameter('gmaps')

        self.gmaps = googlemaps.Client(key=config_param['api_key'])
        self.country = config_param['country']

    def lookUpLocation(self, location_string):
        """ Search for a location and return lat/long
        :param location_string: place names (string)
        :return latlong: latitude and longitude (string)
        """
        location_string = location_string + self.country
        geocode_result = self.gmaps.geocode(location_string)
        for data in geocode_result:
            return(data['geometry']['location'])

# PoC
#gm = Gmaps()
#print(gm.lookUpLocation('Helligvaer')