# Generated by Django 4.0 on 2022-01-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_topic_posttopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='heading',
            field=models.CharField(default='', max_length=48),
            preserve_default=False,
        ),
    ]
