from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from animatronics.models import Category, Manufacturer
from core.context_processors import global_context


class ContextProcessorTests(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		Category.objects.create(name='TestCat')
		Manufacturer.objects.create(name='TestMaker', country='CL')

	def test_global_context_contains_categories_and_manufacturers(self):
		request = self.factory.get('/')
		# RequestFactory request doesn't include .user by default
		request.user = AnonymousUser()
		ctx = global_context(request)
		self.assertIn('categories', ctx)
		self.assertIn('manufacturers', ctx)
		self.assertTrue(len(list(ctx['categories'])) >= 1)
		self.assertTrue(len(list(ctx['manufacturers'])) >= 1)
