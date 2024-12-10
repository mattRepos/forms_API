from django.urls import path
from .views import FormsView

urlpatterns = [
    path("get_form/", FormsView.as_view())
]
