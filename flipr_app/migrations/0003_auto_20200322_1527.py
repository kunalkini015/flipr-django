# Generated by Django 2.2.6 on 2020-03-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipr_app', '0002_auto_20200322_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamboardmember',
            name='user',
        ),
        migrations.AddField(
            model_name='teamboardmember',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
