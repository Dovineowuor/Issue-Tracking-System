from django.test import TestCase
from django.apps import apps


# Create your tests here.
from django.test import TestCase
from apps.Projects.models import Project, Issue, Comment, File

class ProjectModelTestCase(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name='Test Project',
            description='A project for testing purposes'
        )

    def test_project_creation(self):
        """Test that a project can be created"""
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().name, 'Test Project')
        self.assertEqual(Project.objects.get().description, 'A project for testing purposes')

    def test_project_string_representation(self):
        """Test that a project's string representation is correct"""
        self.assertEqual(str(self.project), 'Test Project')

class IssueModelTestCase(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name='Test Project',
            description='A project for testing purposes'
        )
        self.issue = Issue.objects.create(
            title='Test Issue',
            description='An issue for testing purposes',
            project=self.project,
            assigned_to=self.project.manager,
            created_by=self.project.manager
        )

    def test_issue_creation(self):
        """Test that an issue can be created"""
        self.assertEqual(Issue.objects.count(), 1)
        self.assertEqual(Issue.objects.get().title, 'Test Issue')
        self.assertEqual(Issue.objects.get().description, 'An issue for testing purposes')

    def test_issue_string_representation(self):
        """Test that an issue's string representation is correct"""
        self.assertEqual(str(self.issue), 'Test Issue')

class CommentModelTestCase(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name='Test Project',
            description='A project for testing purposes'
        )
        self.issue = Issue.objects.create(
            title='Test Issue',
            description='An issue for testing purposes',
            project=self.project,
            assigned_to=self.project.manager,
            created_by=self.project.manager
        )
        self.comment = Comment.objects.create(
            text='Test Comment',
            author=self.project.manager,
            issue=self.issue
        )

    def test_comment_creation(self):
        """Test that a comment can be created"""
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().text, 'Test Comment')

    def test_comment_string_representation(self):
        """Test that a comment's string representation is correct"""
        self.assertEqual(str(self.comment), 'Test Comment')

class FileModelTestCase(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name='Test Project',
            description='A project for testing purposes'
        )
        self.issue = Issue.objects.create(
            title='Test Issue',
            description='An issue for testing purposes',
            project=self.project,
            assigned_to=self.project.manager,
            created_by=self.project.manager
        )
        self.file = File.objects.create(
            name='Test File',
            file='test_file.txt',
            issue=self.issue
        )

    def test_file_creation(self):
        """Test that a file can be created"""
        self.assertEqual(File.objects.count(), 1)
        self.assertEqual(File.objects.get().name, 'Test File')

    def test_file_string_representation(self):
        """Test that a file's string representation is correct"""
        self.assertEqual(str(self.file), 'Test File')

if __name__ == '__main__':
    import unittest
    unittest.main()
