# Generated by Django 3.1.7 on 2021-04-09 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210410_0336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Image',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Title',
            new_name='title',
        ),
    ]
