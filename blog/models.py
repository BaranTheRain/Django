from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class comment(models.Model):
    title=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField()
    is_validate=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.body[:20]
