#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Ce fichier contient une classe représentant un message textuel envoyé dans un channel.
    ----- CODE DE LA CLASSE A IMPLEMENTER -----
"""
import json
import sys

from src.libs.Module.data.config import PUBLIC_DIR


class Message:
    def __init__(self, timestamp, msg, sender):
        self.timestamp = timestamp
        self.msg = msg
        self.sender = sender

    def db_formatting(self):
        return {
            "timestamp": str(self.timestamp),
            "msg": self.msg,
            "sender": self.sender
        }

    def send_to_db(self):
        conv_file_path = ""
        if sys.platform == "win32":
            conv_file_path = PUBLIC_DIR + "\\tmp_conversations\\basic.json"
        if sys.platform == "linux":
            conv_file_path = PUBLIC_DIR + "/tmp_conversations/basic.json"
        with open(conv_file_path) as json_file:
            conv = json.load(json_file)

        conv["data"].append(self.db_formatting())

        with open(conv_file_path, 'w') as outfile:
            json.dump(conv, outfile)
