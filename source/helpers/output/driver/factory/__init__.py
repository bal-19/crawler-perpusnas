from exception.exception import OutputDriverNotRecognizeException
from helpers.output.driver.mongo import MongoOutputDriver

class OutputDriverFactory:
    @staticmethod
    def create_output_driver(*args, **kwargs):
        destination = kwargs.get("destination")
        assert destination, "Destination is required"
        if destination == "mongo":
            return OutputDriverFactory.create_mongo_output_driver(*args, **kwargs)
        else:
            raise OutputDriverNotRecognizeException()

    @staticmethod
    def create_mongo_output_driver(*args, **kwargs):
        return MongoOutputDriver(
            collection=kwargs.pop("output"),
            connection_string=kwargs.pop("mongo_connection_string"),
            database=kwargs.pop("mongo_database"),
            *args,
            **kwargs
        )