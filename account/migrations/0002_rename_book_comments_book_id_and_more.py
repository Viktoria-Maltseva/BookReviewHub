# Generated by Django 5.0.3 on 2024-04-03 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='book',
            new_name='book_id',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='user',
            new_name='user_id',
        ),
    ]