# Generated by Django 2.2.12 on 2021-07-11 02:50

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210711_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='alternate_email',
            field=models.EmailField(blank=True, max_length=248, null=True, validators=[blog.validators.validate_kiran]),
        ),
    ]
