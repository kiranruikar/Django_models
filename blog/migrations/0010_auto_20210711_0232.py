# Generated by Django 2.2.12 on 2021-07-11 02:32

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_postmodel_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author_email',
            field=models.CharField(blank=True, max_length=248, null=True, validators=[blog.models.validate_author_email]),
        ),
    ]
