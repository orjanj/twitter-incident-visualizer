#!/usr/bin/python3
import gmaps
from Config import Config # TODO: Make it prettier

class Gmaps:
    """ Base class for connecting and fetching data from Google Maps API. """

    def __init__(self):
        """ Instance constructor
        :return: none
        """
        config = Config()
        config_param = config.getConfigParameter('gmaps')
        self.gmaps_conf = gmaps.configure(api_key=config_param['api_key'])

    def lookUpLocation(location_string):
        """ Search for a location and return lat/long
        :param location_string: place names (string)
        :return latlong: latitude and longitude (json str)
        """

        # TODO: Use Geocoding Google API - URL: https://developers.google.com/maps/documentation/geocoding/usage-and-billing




# REF:
# https://github.com/googlemaps/google-maps-services-python