from ..repository.tiny_forms_repository import TinyDBFormsRepository


class FormsManager:

    def __init__(self, repository: TinyDBFormsRepository):
        self.repository = repository

    def load_initial_data(self):
        """Загрузка начальных данных в базу."""
        self.repository.clear_db()

        self.repository.insert_form(
            "Contact Form",
            {"email": "email", "phone_number": "phone"}
        )
        self.repository.insert_form(
            "Order Form",
            {"order_date": "date", "user_email": "email"}
        )

