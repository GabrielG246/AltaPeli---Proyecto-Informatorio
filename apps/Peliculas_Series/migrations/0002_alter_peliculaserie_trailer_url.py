# Generated by Django 5.1.1 on 2024-10-21 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas_Series', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculaserie',
            name='trailer_url',
            field=models.URLField(blank=True, default='https://altapelibucket.s3.us-east-2.amazonaws.com/RickRoll.mp4', max_length=500),
        ),
    ]
