# Generated by Django 4.0.3 on 2022-03-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaylistTrack',
            fields=[
                ('playlistid', models.AutoField(db_column='PlaylistId', primary_key=True, serialize=False)),
                ('trackid', models.IntegerField(db_column='TrackId')),
            ],
            options={
                'db_table': 'playlist_track',
                'managed': False,
            },
        ),
    ]
