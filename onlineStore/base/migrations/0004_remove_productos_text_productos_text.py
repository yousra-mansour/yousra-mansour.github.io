# Generated by Django 4.0.3 on 2022-07-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_test_productos_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='text',
        ),
        migrations.AddField(
            model_name='productos',
            name='text',
            field=models.ManyToManyField(to='base.test'),
        ),
    ]
