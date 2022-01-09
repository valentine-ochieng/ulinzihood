# Generated by Django 3.2.9 on 2022-01-09 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20220109_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='image',
            field=models.ImageField(blank=True, default='biz_pic/bizpic.jpg', upload_to='biz_pic/'),
        ),
        migrations.AlterField(
            model_name='facilities',
            name='image',
            field=models.ImageField(blank=True, default='facilities/sample.jpg', upload_to='facilities'),
        ),
        migrations.AlterField(
            model_name='hood',
            name='image',
            field=models.ImageField(blank=True, default='hood_photo/hood.jpg', upload_to='hood_photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile_photo/defaultprofile.jpg', upload_to='profile_photo'),
        ),
    ]
