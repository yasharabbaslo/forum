from django.test import TestCase
from django.urls import reverse
from .models import Board


class IndexTest(TestCase):
    def setUp(self):
        self.board = Board.objects.create(
            name='Django', description='Django Board')

    def index_view_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def index_view_contains_links_to_topics_page(self):
        response = self.client.get(reverse('index'))
        board_toics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(response, 'href="{0}"'.format(board_toics_url))


class BoardTopicTEsts(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django Board')

    def board_topics_view_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
