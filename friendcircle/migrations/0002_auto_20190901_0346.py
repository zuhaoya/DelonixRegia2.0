# Generated by Django 2.2.4 on 2019-09-01 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendcircle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendpost',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]