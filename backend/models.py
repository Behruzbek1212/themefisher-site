from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    img = models.TextField()

    def __str__(self):
        return self.name
    

class KeyPost(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name