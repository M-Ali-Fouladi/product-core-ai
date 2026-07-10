from abc import ABC, abstractmethod


class BaseImporter(ABC):

    @abstractmethod
    def import_product(self, url: str) -> dict:
        pass
