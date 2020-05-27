from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

app_name = 'primary'

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='', blank=True)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/img', blank=True)
    title = models.CharField(max_length=200)
    video = EmbedVideoField(blank=True, null=True)
    description = models.TextField()
    additional_information = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    price = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('primary:post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



class Comment(models.Model):
    image = models.ImageField(upload_to='static/img/blog', blank=True)
    post = models.ForeignKey('primary.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("primary:post_list")

    def __str__(self):
        return self.text



class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

class Contact(models.Model):
    contact_name = models.CharField(blank=False, max_length=30)
    contact_email = models.EmailField(blank=False)
    def __str__(self):
        return self.Email
    contact_subject = models.CharField(blank=False, max_length=200)
    contact_message = models.TextField(blank=False)
