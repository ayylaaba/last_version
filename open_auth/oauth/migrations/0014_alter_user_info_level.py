# Generated by Django 4.2.10 on 2024-11-24 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0013_user_info_draw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='level',
            field=models.IntegerField(default=20),
        ),
    ]
