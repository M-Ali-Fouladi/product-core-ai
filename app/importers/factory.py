from .mock import MockImporter


class ImportFactory:

    @staticmethod
    def get_importer(store: str):

        if store == "mock":
            return MockImporter()

        raise Exception("Unsupported Store")
