from tinydb import TinyDB, Query
from .repository import AbstractRepository

class TinyDBFormsRepository(AbstractRepository):
    
    def __init__(self, db: TinyDB):
        self.table = db.table('forms')

    def insert_form(self, name: str, fields: dict):
        self.table.insert({"name": name, "fields": fields})
    
    def get_form_by_fields(self, fields: dict):
        Form = Query()
        return self.table.get(Form.fields == fields)
    
    def clear_db(self):
        self.table.truncate()