from django.db import models
# added below
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from djrichtextfield.models import RichTextField
# from ckeditor.fields import RichTextField

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    contributor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="csiblog_posts")
    date = models.DateTimeField(auto_created=True)
    revised = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    content = RichTextField(max_length=5000, blank=True, null=True)
    no_of_likes = models.ManyToManyField(
        User, related_name="csiblog_no_of_likes")
    excerpt = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name + ' |  ' + (str(self.contributor))

    def no_of_likes(self):
        return self.no_of_likes.count()
