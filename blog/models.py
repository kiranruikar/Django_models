from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from .validators import validate_author_email, validate_kiran
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save

"""
python3 manage.py makemigrations # every time you change model.py
python manage.py migrate
"""

PUBLISH_CHOICES = [
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
]


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    # id = models.IntegerField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=200,
                             verbose_name="Post Title",
                             unique=True,
                             error_messages={
                                 'unique': "This title is not unique, please try something else "
                             },
                             help_text="must be a unique title")

    # help_text lets us add the help text under the field
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(editable=True, null=True, blank=True)
    # editable lets us edit the field manually
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.CharField(max_length=248, validators=[validate_author_email, validate_kiran], null=True,
                                    blank=True)
    alternate_email = models.EmailField(max_length=248, validators=[validate_kiran], null=True, blank=True)
    # validator lets us validate the the field we entered
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # if not self.slug and self.title:
        #     self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return smart_text(self.title)


def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    print("Before Save")
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)


pre_save.connect(blog_post_model_pre_save_receiver, sender=PostModel)


def blog_post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    print("After Save")
    print(created)
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()


post_save.connect(blog_post_model_post_save_receiver, sender=PostModel)
