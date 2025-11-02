from django.test import TestCase, Client
from animatronics.models import Category, Manufacturer, Animatronic


class AnimatronicsListTests(TestCase):
    def setUp(self):
        cat = Category.objects.create(name='TestCat')
        maker = Manufacturer.objects.create(name='Maker1', country='CL')
        for i in range(15):
            Animatronic.objects.create(name=f'A{i}', description='x', price=10, category=cat, manufacturer=maker, stock=5)

    def test_list_status_and_pagination(self):
        c = Client()
        resp = c.get('/animatronics/')
        self.assertEqual(resp.status_code, 200)
        # page_obj should be in context
        self.assertIn('page_obj', resp.context)
        self.assertEqual(len(resp.context['page_obj'].object_list), 10)

    def test_second_page(self):
        c = Client()
        resp = c.get('/animatronics/?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('page_obj', resp.context)
        self.assertEqual(len(resp.context['page_obj'].object_list), 5)
