# Generated by Django 3.1 on 2020-08-04 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_stickynote_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='stickynote',
            name='x',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stickynote',
            name='y',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]