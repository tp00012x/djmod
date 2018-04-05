from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from .validators import validate_justin, validate_author_email

PUBLISH_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
        ('private', 'Private')
    )


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=255, default='New Title', unique=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, default='draft', choices=PUBLISH_CHOICES)
    view_count = models.IntegerField(default=0)
    publish_data = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(max_length=240, null=True, blank=True, validators=[validate_justin])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return smart_text(self.title)
