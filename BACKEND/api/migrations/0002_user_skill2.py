# Generated by Django 4.0.6 on 2022-09-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='skill2',
            field=models.BooleanField(default=False),
        ),
    ]
