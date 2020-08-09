# Generated by Django 3.1 on 2020-08-08 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0009_stickynote_zindex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stickynote',
            name='zIndex',
        ),
        migrations.AddField(
            model_name='stickynote',
            name='zindex',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]