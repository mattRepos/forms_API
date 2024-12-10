from datetime import datetime
import re

class FormValueValidator:
    
    def __init__(self, value: str):
        self.value = value

    def is_date(self) -> bool:
        try:
            datetime.strptime(self.value, '%d.%m.%Y')
            return True
        except ValueError:
            pass
        try:
            datetime.strptime(self.value, '%Y-%m-%d')
            return True
        except ValueError:
            pass
        return False
    
    def is_email(self) -> bool:
        return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', self.value))
    
    def is_phone(self) -> bool:
        return bool(re.match(r'^\+7\d{10}$', self.value))

    def validate(self) -> str:
        if self.is_date():
            return "date"
        if self.is_phone():
            return "phone"
        if self.is_email():
            return "email"
        return "text"

