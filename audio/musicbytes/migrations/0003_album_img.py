# Generated by Django 3.2.10 on 2021-12-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbytes', '0002_album_composer'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='img',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
