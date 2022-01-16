# Generated by Django 2.2.12 on 2022-01-15 19:35

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('javatest', '0002_remove_player_pledge5'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='pledge5',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='I checked my internet speed and have a ping speed under 100'),
        ),
    ]
