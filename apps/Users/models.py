from django.db import models
from django.contrib.auth.models import User
from apps.Projects.models import Issue, Project
import redis

# In this updated version, we've added caching for user inputs, requests, and responses.
# For user inputs, we've added a static method get_user_issue that retrieves a single user 
# issue based on the user ID and issue ID. This method checks if the data is in Redis cache and 
# returns it if it is, or retrieves the data from the database, caches it, and returns it if it is 
# not in cache.

# For user requests, we've added a static method get_user_issues that retrieves all user issues
#  based on the user ID. This method works in a similar way to get_user_issue, but retrieves a list 
# of user issues instead of a single issue.

# create Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        # use the default database (sqlite3) for this model
        db_table = "project"

class UserIssue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='assigned_issues_user')
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed')])

    class Meta:
        # use the mysql database for this model
        db_table = "user_issue"
        # set the database to use for this model
        # using = 'mysql'
        # The `using` attribute is no longer needed since it is already specified in the `DATABASES` setting in the settings.py file.

    # add caching for user inputs
    @staticmethod
    def get_user_issue(user_id, issue_id):
        # create cache key
        cache_key = f'user_issue_{user_id}_{issue_id}'

        # check if data is in cache
        cached_data = redis_client.get(cache_key)
        if cached_data:
            # return cached data
            return cached_data.decode('utf-8')
        else:
            # get data from database
            user_issue = UserIssue.objects.get(id=issue_id, assigned_to__assigned_user_id=user_id)

            # cache data
            redis_client.set(cache_key, str(user_issue))

            # return data
            return str(user_issue)

    # add caching for user requests
    @staticmethod
    def get_user_issues(user_id):
        # create cache key
        cache_key = f'user_issues_{user_id}'

        # check if data is in cache
        cached_data = redis_client.get(cache_key)
        if cached_data:
            # return cached data
            return cached_data.decode('utf-8')
        else:
            # get data from database
            user_issues = UserIssue.objects.filter(assigned_to__assigned_user_id=user_id)

            # cache data
            redis_client.set(cache_key, str(user_issues))

            # return data
            return str(user_issues)
