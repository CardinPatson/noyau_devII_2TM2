# -*- coding: utf-8 -*-
from .config import cine_link
import requests

import logging
logger = logging.getLogger("bot")


class RequestError(Exception):
    pass


class Cine:
    def __init__(self, origin='Louvain-la-Neuve'):
        self.__origin = origin
        self.__url_origin = cine_link(self.origin)

    @property
    def url_origin(self):
        return self.__url_origin

    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, origin):
        self.__origin = origin

    def get_cine(self):
        """
        Renvoie une liste de cinémas

        PRE : "/cine"
        POST : liste des cinemas de la localité passée en paramètre (par défaut LLN)
        RAISES : Exception : si pas de réponse à la requete

        """
        response = requests.get(self.url_origin).json()

        if not len(response):
            logger.error("Can't fetch Cinema")
            raise RequestError("Can't fetch Cinema")

        cine = ""
        for i in response:
            cine += "\n"
            for address in i["address"]:
                if address not in ["country", "country_code", "region", "postcode", "county"]:
                    cine += f"{i['address'][address]} "
            cine += "\n"
        return cine
