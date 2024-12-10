from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def get_form_by_fields(self, fields: dict): pass

    @abstractmethod
    def clear_db(self): pass

    @abstractmethod
    def insert_form(self, name: str, fields: dict): pass