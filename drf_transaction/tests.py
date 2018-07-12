from django.test import TestCase
from .models import TransactionModes, TransactionDetails
from datetime import datetime
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase


user1 = get_user_model().objects.create_user(username='test1', email='test1@civilmachines.com', password='123@abcd@123',
                                             name='Test User - 1', mobile='8800610541')
user2 = get_user_model().objects.create_user(username='test2', email='test2@civilmachines.com', password='123@abcd@123',
                                             name='Test User - 2', mobile='8800610542')
user3 = get_user_model().objects.create_user(username='test3', email='test3@civilmachines.com', password='123@abcd@123',
                                             name='Test User - 3', mobile='8800610543')


# class TransactionModesModelTests(TestCase):
#
#     def test(self):
#
#         self.assertEqual(user1.mode,'Cash')

# class ReadModeTests(APITestCase):
#
#     def setUp(self):
#         self.user = user1
#
#     def test_read(self):
#         response = self.user.objects.get(user1.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


class AddTransactionDetailsTest(APITestCase):

    def setUp(self):
        self.user = user1

    def test(self):
        pass


