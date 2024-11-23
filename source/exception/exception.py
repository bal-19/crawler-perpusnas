import re

class OutputDriverNotRecognizeException(Exception):
    def __str__(self):
        return "Destination not recognized"
