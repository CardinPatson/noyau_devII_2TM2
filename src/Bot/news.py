# -*- coding: utf-8 -*-
import requests
import datetime
from .config import news_link

import logging

logger = logging.getLogger("bot")


class ParameterException(Exception):
    pass


class News:
    def __init__(self, arg: str = "be"):
        self.__argument = arg
        self.__date = "&date=" + str(datetime.date.today())
        self.__limit = "&limit=1"
        self.__country = "&countries="
        self.__keyword = "&keywords="
        self.__languages = "&languages=fr"
        self.__api_link = news_link()
    @property
    def date(self):
        return self.__date

    @property
    def limit(self):
        return self.__limit

    @property
    def country(self):
        return self.__country

    @property
    def api_link(self):
        return self.__api_link

    @api_link.setter
    def api_link(self, new_link):
        self.__api_link = new_link

    @property
    def languages(self):
        return self.__languages

    @property
    def argument(self):
        return self.__argument

    @property
    def keyword(self):
        return self.__keyword

    @keyword.setter
    def keyword(self, new_keyword):
        self.__keyword = new_keyword

    @country.setter
    def country(self, new_country):
        self.__country = new_country

    def get_news(self):
        """
        Renvoie les actualites

        PRE : "/news"
        POST : Renvoie une chaine contenant les news d'un pays ou d'un sujet
        RAISES : Exception : si pas de réponse à la requête

        """
        if len(self.argument) == 2:
            self.country = self.country + self.argument
        else:
            self.keyword = self.keyword + self.argument

        try:
            reponse = requests.get(
                self.api_link + self.country + self.languages + self.limit + self.keyword + self.date)

        except ValueError:
            logger.error("News : Can't process to the request")
            return "Erreur dans le get"

        current = reponse.json()

        if current['pagination']['count'] == 0:
            return "Désolé nous n'avons pas trouvé d'article en français pour le pays ou le sujet sélectionné"

        result = ""
        for i in range(current['pagination']['count']):
            result += f"{current['data'][i]['title']}\n" \
                      f"de {current['data'][i]['author']}\n" \
                      f"publié le : {current['data'][i]['published_at']}\n\n" \
                      f"{current['data'][i]['description']}\n\n" \
                      f"url: {current['data'][i]['url']}\n\n\n"

        return result
