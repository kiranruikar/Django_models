# Generated by Django 2.2.12 on 2021-07-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210707_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish'), ('private', 'Private')], default='draft', max_length=120),
        ),
    ]
