# Generated by Django 4.2.1 on 2023-05-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_alter_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.FloatField(default=180),
            preserve_default=False,
        ),
    ]
