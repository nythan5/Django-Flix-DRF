# Generated by Django 5.0.6 on 2024-06-28 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='starts',
            new_name='stars',
        ),
    ]
