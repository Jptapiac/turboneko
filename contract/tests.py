from django.test import TestCase, Client
from .models import Contact


class ContactFormTests(TestCase):
	def test_contact_create_via_client(self):
		c = Client()
		resp = c.post('/contacto/', {'name': 'QA Tester', 'email': 'qa@example.com', 'subject': 'Test', 'message': 'Hola prueba'}, follow=True)
		self.assertIn(resp.status_code, (200, 302))
		exists = Contact.objects.filter(email='qa@example.com', subject='Test').exists()
		self.assertTrue(exists)

	def test_contact_model_str(self):
		contact = Contact.objects.create(name='Alice', email='alice@example.com', subject='Hola', message='Mensaje')
		self.assertIn('Alice', str(contact))
