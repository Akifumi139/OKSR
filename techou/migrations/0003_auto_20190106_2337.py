# Generated by Django 2.1.5 on 2019-01-06 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techou', '0002_auto_20190106_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='created_at',
            new_name='purchase_date',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='message',
            name='medicine_name',
            field=models.CharField(default=1, max_length=510),
            preserve_default=False,
        ),
    ]
