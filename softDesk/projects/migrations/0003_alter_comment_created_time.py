# Generated by Django 4.2 on 2023-04-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_issue_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
