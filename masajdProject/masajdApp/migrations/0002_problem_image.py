# Generated by Django 4.1.3 on 2022-11-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masajdApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/images/'),
            preserve_default=False,
        ),
    ]
