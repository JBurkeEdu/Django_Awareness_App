# Generated by Django 2.0.2 on 2018-07-10 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180704_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone',
            new_name='age',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='description',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
