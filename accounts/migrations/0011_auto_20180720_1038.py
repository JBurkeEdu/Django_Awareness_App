# Generated by Django 2.0.2 on 2018-07-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20180720_1016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailtext',
            options={'verbose_name': 'Send Email to All Users', 'verbose_name_plural': 'Send Email to All Users'},
        ),
        migrations.RemoveField(
            model_name='mailtext',
            name='attachment',
        ),
        migrations.AlterField(
            model_name='mailtext',
            name='message',
            field=models.TextField(max_length=1000),
        ),
    ]
