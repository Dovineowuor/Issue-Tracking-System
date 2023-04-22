from django.test import TestCase
from apps.Projects.models import Board

class BoardTestCase(TestCase):
    def setUp(self):
        self.board_name = "Test Board"

    def test_create_board(self):
        # Create a new board
        board = Board.objects.create(name=self.board_name)

        # Verify that the board is added to the list of boards
        response = self.client.get('/boards/')
        self.assertContains(response, self.board_name)

        # Verify that the board name is displayed correctly
        response = self.client.get(f'/boards/{board.id}/')
        self.assertContains(response, self.board_name)

        # Verify that the board can be edited and saved successfully
        new_board_name = "New Board Name"
        response = self.client.post(f'/boards/{board.id}/edit/', {'name': new_board_name})
        self.assertEqual(response.status_code, 302)
        board.refresh_from_db()
        self.assertEqual(board.name, new_board_name)

        # Verify that the board can be deleted and removed from the list of boards
        response = self.client.post(f'/boards/{board.id}/delete/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/boards/')
        self.assertNotContains(response, self.board_name)