# -*- coding: utf-8 -*-
from .config import check_conection
import logging


logger = logging.getLogger("bot")


class ParameterException(Exception):
    pass


class Request:
    def __init__(self, message: str):
        self.__message = message

    @property
    def message(self):
        return self.__message
    
    def set_message(self, message: str):
        self.__message = message

    def get_message(self, command_list):
        """
        Renvoie la liste des commandes et récupère la request de l'utilisateur

        PRE : une commande de la liste help précédée d'un /
        POST : renvoie la liste des mots composant la commande
        RAISES : RAISES : Exception : si pas de réponse à la requête

        """
        if check_conection():
            logger.error("Error connection")
            self.set_message("Please check your internet connection")
            return self.message
        message_words = self.message.split(" ")
        if message_words[0][0] == "/" and message_words[0] in command_list:
            return message_words

        elif message_words[0][0] == "/" and message_words[0] not in command_list:
            self.set_message("Commande introuvable! Entrez /help pour voir la liste des commandes")
            return self.message
        else:
            logger.warning("Commande introuvable!!")
            self.set_message("Commande introuvable! Entrez /help pour voir la liste des commandes")
            return self.message
