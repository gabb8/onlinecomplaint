# Generated by Django 2.2.16 on 2020-11-30 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_app', '0002_complaint_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='userstatus',
            field=models.CharField(default='user', max_length=150),
        ),
    ]
