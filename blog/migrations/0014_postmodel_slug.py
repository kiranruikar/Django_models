# Generated by Django 2.2.12 on 2021-07-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_postmodel_alternate_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
