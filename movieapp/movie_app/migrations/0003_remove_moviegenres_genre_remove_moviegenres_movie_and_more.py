# Generated by Django 4.0.2 on 2022-02-13 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_alter_moviedata_director_alter_moviedata_star1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviegenres',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='moviegenres',
            name='movie',
        ),
        migrations.AddField(
            model_name='moviedata',
            name='genre',
            field=models.CharField(default=' ', max_length=128),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='MovieGenres',
        ),
    ]
