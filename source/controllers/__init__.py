import random
import time
import re

from faker import Faker
from loguru import logger
from abc import ABC
from configparser import ConfigParser
from helpers.output import Output


class Controllers(ABC):
    def __init__(self, *args, **kwargs):
        self.config = ConfigParser()
        self.config.read(kwargs.get("config"))
        self.faker = Faker()
        self.log = logger

        if kwargs.get("destination"):
            if kwargs.get("destination") == "mongo":
                kwargs.update({
                    "mongo_database": self.config.get("mongo", "database"),
                    "mongo_connection_string": self.config.get("mongo", "connection_string")
                })
            
            self.output_name = kwargs.get("output")
            self.destination_name = kwargs.get("destination")
            self.output = Output(*args, **kwargs)

    async def main(self):
        try:
            await self.handler()
        except Exception as e:
            self.exceptions_handler(e)

    async def handler(self):
        pass

    def exceptions_handler(self, e):
        self.log.error(e)