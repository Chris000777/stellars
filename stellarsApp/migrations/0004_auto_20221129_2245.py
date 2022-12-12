# Generated by Django 3.2.14 on 2022-11-30 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stellarsApp', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
