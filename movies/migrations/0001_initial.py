# Generated by Django 4.2.1 on 2023-05-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_adi', models.CharField(max_length=100)),
                ('aciklama', models.TextField()),
                ('gorsel', models.CharField(max_length=100)),
                ('anasayfa', models.BooleanField(default=False)),
            ],
        ),
    ]
