from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class TaskCreationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            'roberto',
            'roberto@admin.com',
            'roberto123'
        )

        self.token = Token.objects.get(user=self.user)

    def testcase_create_one(self):
        self.client.force_login(user=self.user)
        response = self.client.post(
            '/tasks/',
            data={'title': "Get to work"},
            format='json',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(response.status_code, 201)

    def testcase_retrieve_all(self):
        self.client.force_login(user=self.user)
        response = self.client.get(
            '/tasks/',
            format='json',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(response.status_code, 200)

    def testcase_retrieve_one(self):
        self.client.force_login(user=self.user)
        response = self.client.get(
            '/tasks/',
            data={'id':1},
            format='json',
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(response.status_code, 200)






