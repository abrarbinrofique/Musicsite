# Generated by Django 4.2.11 on 2024-06-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=20)),
                ('Lastname', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Phonenumber', models.IntegerField(max_length=20)),
                ('Instrument', models.CharField(max_length=20)),
            ],
        ),
    ]
