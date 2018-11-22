from django.test import TestCase, Client
from django.urls import reverse

from .models import Mineral


class TestMinerals(TestCase):
    def setUp(self):
        """sets up a fake mineral object for testing"""
        self.mineral = Mineral.objects.create(name="test mineral",
                                              image_caption="caption test",
                                              category="test category")
        self.client = Client()

    def test_mineral_list_view(self):
        """tests the view with a list of minerals"""
        resp = self.client.get(reverse('list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        assert isinstance(resp.context['rnd_pk'], int)

    def test_mineral_details_view(self):
        """tests the view that shows each mineral's details"""
        resp = self.client.get(reverse('detail', kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral.name, resp.context.get('name'))
        self.assertEqual(self.mineral.image_caption, resp.context.get('image_caption'))
        self.assertIn(self.mineral.category, resp.context.get('mineral_dict').get('Category'))
        assert isinstance(resp.context['rnd_pk'], int)
