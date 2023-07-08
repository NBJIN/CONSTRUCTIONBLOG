from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    contributor = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1)
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
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('postread', kwargs={'pk': self.pk})

    # def no_of_likes_count(self):
    #     return self.no_of_likes.all().count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="csiblog_comment")
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_author")
    added = models.DateTimeField(auto_created=True)
    mainbody = RichTextField(max_length=5000, blank=True, null=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-added']

    def __str__(self):
        return self.title + ' | ' + (str(self.author))


class PostLike(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="csiblog_like")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' |' + (str(self.post.name))

    # def no_of_likes_count(self):
    #     return self.no_of_likes.all().count()
