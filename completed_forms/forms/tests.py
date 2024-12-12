from django.test import TestCase
from django.urls import reverse

class ApiTestCase(TestCase):
    help= "Тестирование API"

    def test_post_without_formkey(self):

        url = reverse('api_v1')

        test_body = {
            "missing_form": {
                "order_date": "2014-12-01",
                "user_email": "laasdasd@mail.com",
                "asdasd": "qasdasdasd"
            }
        }

        response = self.client.post(url, test_body, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"form":["This field is required."]})
    

    def test_post_form(self):

        url = reverse('api_v1')
        test_body = {
            "form": {
                "order_date": "2014-12-01",
                "user_email": "laasdasd@mail.com",
                "asdasd": "qasdasdasd"
            }
        }
    
        response = self.client.post(url, test_body, content_type='application/json')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), {"form":{"fields":{"order_date":"date","user_email":"email","asdasd":"text"}}})

    def test_post_form_not_identificate_form(self):

        url = reverse('api_v1')

        test_body = {
            "form":{
                "order_date": "2014-12-01",
                "user_email": "laasdasd@mail.com",
                "asdasd": "asdasd"
            }
        }

        response = self.client.post(url, test_body, content_type='application/json')

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{
            "form": {
                "fields": {
                    "order_date": "date",
                    "user_email": "email",
                    "asdasd": "text"
                }
            }
        }
        )