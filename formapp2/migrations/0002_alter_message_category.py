# Generated by Django 4.0.3 on 2022-04-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='category',
            field=models.CharField(choices=[('q', 'Pytanie'), ('o', 'Inne')], max_length=10),
        ),
    ]
