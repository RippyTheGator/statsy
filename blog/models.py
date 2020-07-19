from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Update(models.Model):

    update_title = models.CharField(max_length=50)
    update_content = models.TextField()
    update_username = models.ForeignKey(User, on_delete=models.CASCADE)
    update_published = models.DateTimeField("date published", default=timezone.now)

    def __str__(self):
        return self.update_title
