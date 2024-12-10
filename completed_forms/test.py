from forms.repository import db
from forms.services.forms_service import FormsService

service = FormsService(db.forms)

service.get_form_by_fields({
    "zalupa": "alskjdlas@mail.com",
    "penis": "+79831656419"
})