from django.db import models


class Update(models.Model):

    update_title = models.CharField(max_length=50)
    update_content = models.TextField()
    update_published = models.DateTimeField("date published")

    def __str__(self):
        return self.update_title
