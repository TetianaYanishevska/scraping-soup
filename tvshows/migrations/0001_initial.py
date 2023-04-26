# Generated by Django 4.2 on 2023-04-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_image', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
    ]
