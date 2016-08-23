from django.test import TestCase, Client
from .models import Membership
import paypal.standard.forms
from paypal.standard.forms import PayPalPaymentsForm
from django import forms
from django.conf import settings
from django.db import models
import unittest
from unittest import TestCase
from . import views
from .admin import BookAdmin
from memberships.views import all_memberships
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory


def test_membership_page_status_code_is_ok(self):
    home_page = self.client.get('/')
    self.assertEquals(home_page.status_code, 200)


def test_membership_page_content_is_correct(self):
    home_page = self.client.get('/memberships/')
    self.assertTemplateUsed(home_page, "/templates/memberships/memberships.html")
    home_page_template_output = render_to_response("/templates/memberships/memberships.html", {'user': self.user}).content
    self.assertEquals(home_page.content, home_page_template_output)


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='None', email='none@none.com', password='letmein1')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/templates/memberships/memberships.html')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = views(request)
        # Use this syntax for class-based views.
        response = views.as_view()(request)
        self.assertEqual(response.status_code, 200)









