from django.core.management.base import BaseCommand
from forms.repository import db
from forms.managers.forms_manager import FormsManager

class Command(BaseCommand):
    help = 'Инициализирует таблицу с формами'

    def handle(self, *args, **kwargs):
        forms_repository = db.forms
        forms_manager = FormsManager(forms_repository)
        forms_manager.load_initial_data()