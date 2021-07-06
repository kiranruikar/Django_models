from django.db import models
from django.db.models import Model

"""
python3 manage.py makemigrations # every time you change model.py
python manage.py migrate
"""


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    # id = models.IntegerField(primary_key=True)
    active = models.BooleanField(default=True)

    pass

