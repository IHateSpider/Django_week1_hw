# Generated by Django 2.1.1 on 2018-10-11 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textmessage',
            old_name='speaker',
            new_name='talker',
        ),
    ]
