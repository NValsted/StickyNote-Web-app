# Generated by Django 3.1 on 2020-08-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20200805_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickynote',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stickynote',
            name='x',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stickynote',
            name='y',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]