# Generated by Django 4.2.7 on 2023-12-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='school',
            fields=[
                ('Sname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Slocation', models.CharField(max_length=100)),
                ('Sprincipal', models.CharField(max_length=100)),
            ],
        ),
    ]