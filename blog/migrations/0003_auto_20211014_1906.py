# Generated by Django 3.2.5 on 2021-10-14 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_img_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_header',
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
    ]
