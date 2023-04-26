from http.client import responses
from django.test import TestCase, override_settings
from Board.models import Board, Project, Task, User, Comment
from django.test.runner import DiscoverRunner
import django

#@override_settings(INSTALLED_APPS=['Board'])
class MyAppTestCase(django.test.TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create(username='testuser')

        # Create a board
        self.board_name = "Test Board"
        self.board = Board.objects.create(name=self.board_name)

        # Create a project
        self.project_name = "Test Project"
        self.project = Project.objects.create(name=self.project_name)

        # Create a task
        self.task_name = "Test Task"
        self.task = Task.objects.create(name=self.task_name)

        # Assign the task to the project and board
        self.task.projects.add(self.project)
        self.task.boards.add(self.board)

        # Assign the task to the user
        self.task.assigned_to.add(self.user)

        # Create a comment
        self.comment_text = "Test Comment"
        self.comment = Comment.objects.create(text=self.comment_text, task=self.task, user=self.user)

    def tearDown(self):
        # Delete test data
        self.user.delete()
        self.board.delete()
        self.project.delete()
        self.task.delete()
        self.comment.delete()

    def test_board_functionality(self):
        print("Running test_board_functionality...")
        # Verify board creation
        response = self.client.get('/boards/')
        self.assertContains(response, self.board_name)

        # Verify board editing
        new_board_name = "New Board Name"
        response = self.client.post(f'/boards/{self.board.id}/edit/', {'name': new_board_name})
        self.assertEqual(response.status_code, 302)
        self.board.refresh_from_db()
        self.assertEqual(self.board.name, new_board_name)

        # Verify board deletion
        response = self.client.post(f'/boards/{self.board.id}/delete/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/boards/')
        self.assertNotContains(response, self.board_name)
        print("test_board_functionality passed.")

    def test_project_functionality(self):
        print("Running test_project_functionality...")
        # Verify project creation
        response = self.client.get('/projects/')
        self.assertContains(response, self.project_name)

        # Verify project editing
        new_project_name = "New Project Name"
        response = self.client.post(f'/projects/{self.project.id}/edit/', {'name': new_project_name})
        self.assertEqual(response.status_code, 302)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, new_project_name)

        # Verify project deletion
        response = self.client.post(f'/projects/{self.project.id}/delete/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/projects/')
        self.assertNotContains(response, self.project_name)
        print("test_project_functionality passed.")

    def test_task_functionality(self):
        print("Running test_task_functionality...")
        # Verify task creation
        response = self.client.get('/tasks/')
        self.assertContains(response, self.task_name)

        # Verify task editing
        new_task_name = "New Task Name"
        response = self.client.post(f'/tasks/{self.task.id}/edit/', {'name': new_task_name})
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, new_task_name)

        # Verify task deletion
        response = self.client.post(f'/tasks/{self.task.id}/delete/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/tasks/')
        self.assertNotContains(response, self.task_name)

        # Verify task assignment
        response = self.client.get(f'/tasks/{self.task.id}/')
        self.assertContains(response, self.user.username)

        # Verify task status change
        response = self.client.post(f'/tasks/{self.task.id}/change_status/', {'status': 'completed'})
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/tasks/')
        self.assertNotContains(response, self.task_name)
        print("test_task_functionality passed.")

    def test_user_functionality(self):
        print("Running test_user_functionality...")
        # Verify user creation
        response = self.client.get('/users/')
        self.assertContains(response, self.user.username)

        # Verify user editing
        new_username = "newuser"
        response = self.client.post(f'/users/{self.user.id}/edit/', {'username': new_username})
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, new_username)

        # Verify user deletion
        response = self.client.post(f'/users/{self.user.id}/delete/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/users/')
        self.assertNotContains(responses, self.user.username)
        print("test_user_functionality passed.")

def test_comment_functionality(self):
    print("Running test_comment_functionality...")
    # Verify comment creation
    response = self.client.get(f'/tasks/{self.task.id}/')
    self.assertContains(response, self.comment_text)

    # Verify comment editing
    new_comment_text = "New Comment"
    response = self.client.post(f'/comments/{self.comment.id}/edit/', {'text': new_comment_text})
    self.assertEqual(response.status_code, 302)
    self.comment.refresh_from_db()
    self.assertEqual(self.comment.text, new_comment_text)

    # Verify comment deletion
    response = self.client.post(f'/comments/{self.comment.id}/delete/')
    self.assertEqual(response.status_code, 302)
    response = self.client.get(f'/tasks/{self.task.id}/')
    self.assertNotContains(response, self.comment_text)
    print("test_comment_functionality passed.")

def main():
    runner = DiscoverRunner(verbosity=2)
    failures = runner.run_tests(['Board'])
    if failures:
        print('Tests failed')
    else:
        print('All tests passed')

if __name__ == '__main__':
    main()