from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='tasks', on_delete = models.CASCADE)

    class Meta:
        ordering = ( 'title',)
