# Generated by Django 4.2.7 on 2023-11-18 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_room_created_at_alter_room_votes_to_skip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='votes_to_skip',
            field=models.DateTimeField(default=1),
        ),
    ]
