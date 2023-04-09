from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory

from admin_tool_button.contrib.admin import ButtonActionAdmin


class UserAdmin(ButtonActionAdmin):

    button_actions = ['add_user']

    def add_user(self, request):
        User.objects.create_user('tester')


class TestAdmin(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.site = AdminSite()
        self.user = User.objects.create_superuser('johndoe')

    def test_changelist(self):
        admin = UserAdmin(User, self.site)
        request = RequestFactory().get("/")
        request.user = self.user
        response = admin.changelist_view(request)
        self.assertEqual(response.status_code, 200)
        response.render()
        self.assertContains(response, 'add_user')

    def test_button_action(self):
        admin = UserAdmin(User, self.site)
        request = RequestFactory().post("/", {'button_action': 'add_user'})
        request.user = self.user
        request._dont_enforce_csrf_checks = True
        response = admin.changelist_view(request)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='tester').exists())

    def test_invalid_button_action(self):
        admin = UserAdmin(User, self.site)
        request = RequestFactory().post("/", {'button_action': 'foo'})
        request.user = self.user
        request._dont_enforce_csrf_checks = True
        response = admin.changelist_view(request)
        self.assertEqual(response.status_code, 302)
