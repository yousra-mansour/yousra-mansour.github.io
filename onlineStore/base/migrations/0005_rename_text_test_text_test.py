# Generated by Django 4.0.3 on 2022-07-13 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_productos_text_productos_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='text',
            new_name='text_test',
        ),
    ]
