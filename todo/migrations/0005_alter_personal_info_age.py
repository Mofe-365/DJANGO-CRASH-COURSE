# Generated by Django 3.2.8 on 2021-10-30 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_personal_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='age',
            field=models.IntegerField(default=15),
        ),
    ]
