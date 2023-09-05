from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tasks(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null =True)
    Title = models.CharField(max_length=30)
    Description = models.TextField (blank=True , null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

    class Meta :
        ordering = ['complete']
