# Generated by Django 2.2.12 on 2021-07-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
