# Generated by Django 3.2 on 2024-02-25 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20240224_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(upload_to='rooms'),
        ),
    ]
