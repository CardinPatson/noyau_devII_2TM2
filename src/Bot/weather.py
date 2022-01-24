import requests
import logging
from .codesTemps import codesTemps
from .config import weather_stack

logger = logging.getLogger("bot")


class ParameterException(Exception):
    pass


class Weather:
    def __init__(self, city="louvain-la-neuve"):
        self.__city = city
        self.__api_link = weather_stack(city)

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def api_link(self):
        return self.__api_link

    @api_link.setter
    def api_link(self, api_link):
        self.__api_link = api_link

    def get_weather(self):
        """
        Renvoie la température de la ville et le temps de la ville

        PRE : "/weather"
        POST : Une chaine de caractère contenant la température et la couverture nuageuse de la localité
        RAISES : Exception : si pas de réponse à la requete

        """

        try:
            response = requests.get(self.api_link)
        except ValueError:
            logger.error("Weather : Can't process the api request")
            return "Erreur dans le get"

        current = response.json()
        print(current)
        return f"La température de {self.city} est de {current['current']['temperature']}°C et " \
               f"il fait {codesTemps[current['current']['weather_code']]}"
