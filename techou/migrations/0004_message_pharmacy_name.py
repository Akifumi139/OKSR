# Generated by Django 2.1.5 on 2019-01-06 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techou', '0003_auto_20190106_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='pharmacy_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
