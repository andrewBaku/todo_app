from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_done = models.BooleanField(default=False)

    def done_problem(self):
        self.is_done = True
        self.save()

    def __str__(self):
        return self.title