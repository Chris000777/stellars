# Generated by Django 3.2.14 on 2022-12-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stellarsApp', '0004_auto_20221129_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alta',
            field=models.BooleanField(default=1),
        ),
    ]