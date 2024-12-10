from ..repository.tiny_forms_repository import TinyDBFormsRepository
from ..validators.form_value_validator  import FormValueValidator

class FormsService:

    def __init__(self, repository: TinyDBFormsRepository):
        self.repository = repository

    def get_form_by_fields(self, initial_fields: dict) -> dict:
        fields = {}
        for key, value in initial_fields.items():
            validator = FormValueValidator(value)
            fields[key] = validator.validate()
        form_from_db = self.repository.get_form_by_fields(fields)
        if form_from_db:
            return form_from_db
        return {"fields": fields}
    
