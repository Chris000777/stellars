# Generated by Django 3.2.14 on 2022-11-28 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stellarsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
