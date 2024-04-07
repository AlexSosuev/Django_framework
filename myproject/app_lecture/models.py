from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'
    
    def get_summary(self):
        words = self.content.split()
        return f'{"".join(words[:12])}...'
    
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    
    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, age: {self.age}'