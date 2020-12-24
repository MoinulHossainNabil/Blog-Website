from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField

User = get_user_model()


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    profile_pic = models.ImageField()

    def __str__(self):
        return str(self.author)


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class PostViewCount(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.author


class Posts(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    content = HTMLField()
    category = models.ManyToManyField(Category)
    upload_date = models.DateTimeField(auto_now_add=True)
    thmbnail = models.ImageField()
    comment = models.IntegerField(default=0)
    featured = models.BooleanField()
    # view_count = models.IntegerField(default=0)
    previous_post = models.ForeignKey('self', related_name='prev', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_details', kwargs={
            'id': self.id
        })

    def get_update_url(self):
        return reverse('post_update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('post_delete', kwargs={
            'id': self.id
        })

    @property
    def get_comments(self):
        return self.postcomments.all()

    @property
    def count_viwes(self):
        return PostViewCount.objects.filter(post=self).count()


class Comments(models.Model):
    post = models.ForeignKey(Posts, related_name='postcomments', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.author)
