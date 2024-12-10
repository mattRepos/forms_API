from tinydb import TinyDB
from .tiny_forms_repository import TinyDBFormsRepository
from completed_forms.settings import TINY_DB_PATH
from typing import Union

class UnsupportDB(Exception):
    pass

class RepositoryNotFound(Exception):
    pass


class RepositoryFabric:

    def __init__(self, db: Union[TinyDB]):
        if type(db) not in [TinyDB]:
            raise UnsupportDB("База данных не поддерживается")
        self.db = db

    @property
    def forms(self):
        if isinstance(self.db, TinyDB):
            return TinyDBFormsRepository(self.db)
        raise RepositoryNotFound(message=f"Репозиторий не найден.")
    

db = RepositoryFabric(TinyDB(TINY_DB_PATH))
