from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Author(models.Model):
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField()
    
    def __str__(self):
        return str(self.author)

class Category(models.Model):
    category_name = models.CharField(max_length= 100)

    def __str__(self):
        return self.category_name

class Posts(models.Model):
    post_author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    body = models.TextField()
    category = models.ManyToManyField(Category)
    upload_date = models.DateTimeField(auto_now_add=True)
    thmbnail = models.ImageField()
    comment = models.IntegerField(default=0)
    featured = models.BooleanField()
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_details', kwargs={
            'id' : self.id
        })
    
