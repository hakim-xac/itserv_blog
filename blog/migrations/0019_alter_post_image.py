# Generated by Django 4.2.1 on 2023-06-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='static/media/photos/%Y/%m/%d'),
        ),
    ]
