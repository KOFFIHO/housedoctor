# Generated by Django 3.1 on 2022-01-04 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacie',
            name='degarde',
            field=models.BooleanField(default=True),
        ),
    ]
