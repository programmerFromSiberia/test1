# Generated by Django 4.2.6 on 2023-12-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genres',
            name='img',
        ),
        migrations.AddField(
            model_name='genres',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='images/'),
        ),
    ]