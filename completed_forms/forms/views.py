from rest_framework.views import APIView
from rest_framework.request import Request
from .serializers import FormRequestSerializer
from .services.forms_service import FormsService
from .repository import db
from rest_framework.response import Response


class FormsView(APIView):

    def post(self, request: Request):

        data = request.data
        serializer = FormRequestSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        form = serializer.validated_data.get("form")

        service = FormsService(db.forms)
        form = service.get_form_by_fields(form)
        
        return Response({
            "form": form
        })