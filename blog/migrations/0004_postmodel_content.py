# Generated by Django 2.2.12 on 2021-07-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
