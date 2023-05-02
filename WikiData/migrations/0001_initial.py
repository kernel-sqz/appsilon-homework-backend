# Generated by Django 4.2 on 2023-05-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.URLField()),
                ('imdb_id', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=128)),
                ('date', models.DateField()),
            ],
            options={
                'unique_together': {('imdb_id', 'title', 'date')},
            },
        ),
    ]
