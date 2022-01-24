
from .config import resto_link
import requests

import logging

logger = logging.getLogger("bot")


class RequestError(Exception):
    pass


class Resto:
    def __init__(self, origin='Louvain-la-Neuve'):
        self.__origin = origin
        self.__url_origin = resto_link(self.__origin)

    @property
    def url_origin(self):
        return self.__url_origin

    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, origin):
        self.__origin = origin

    def get_resto(self):
        """
        Renvoie une liste de restos

        PRE : "/resto"
        POST : liste des restos du lieu passé en paramètre (par défaut LLN)
        RAISES : Exception : si pas de réponse à la requete

        """

        response = requests.get(self.url_origin).json()

        if not len(response):
            logger.error("Resto : Can't fetch Restaurant")
            raise RequestError("Can't fetch Restaurant")

        restaurant = ""
        for i in response:
            restaurant += "\n"
            for address in i["address"]:
                if address not in ["country", "country_code", "region", "postcode", "county"]:
                    restaurant += f"{i['address'][address]} "
            restaurant += "\n"
        return restaurant
